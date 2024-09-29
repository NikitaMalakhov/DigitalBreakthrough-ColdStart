from fastapi import FastAPI, Response, Cookie, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
app = FastAPI()
import uuid
from .db import retrieve_db_instance
from .models import VideoData, User, UserInteractions
from mab2rec import BanditRecommender, LearningPolicy, NeighborhoodPolicy
from mab2rec.pipeline import train, score
from mab2rec.utils import save_pickle, load_pickle
import os


rec = load_pickle(os.path.join('.', 'rec.pkl'))



exceptions = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post('/api/{video_id}/{operation}')
async def like(video_id, operation, request: Request, session_id: str = None):
    session = retrieve_db_instance()

    video = session.query(VideoData).filter(VideoData.video_id == video_id).first()
    if not video:
        return {'msg': 'ERR'}
    user_interaction = session.query(UserInteractions).filter(UserInteractions.user_id == uuid.UUID(session_id)).filter(UserInteractions.video_id == video_id).first()

    if user_interaction:
        if not user_interaction.disliked and not user_interaction.liked:
            if operation == 'like':
                video.v_likes += 1
                user_interaction.liked = True
                user_interaction.disliked = False

            else:
                video.v_dislikes += 1
                user_interaction.liked = False
                user_interaction.disliked = True
    else:
        user_interaction = UserInteractions(user_id=uuid.UUID(session_id), video_id=video_id, liked=False, disliked=False)
        if operation == 'like':
            video.v_likes += 1
            user_interaction.liked = True
            user_interaction.disliked = False
        else:
            video.v_dislikes += 1
            user_interaction.liked = False
            user_interaction.disliked = True
        session.add(user_interaction)
    session.commit()
    return video


@app.get('/api/authorize')
async def authorize(response: Response, request: Request, session_id: str = None):
    print(session_id)
    session = retrieve_db_instance()


    if session_id:
        session_id = uuid.UUID(session_id)
        user = session.query(User).filter(User.id == session_id).first()

        if not user:
            user = User()
            session.add(user)
            session.commit()
            session.refresh(user)
            # response.set_cookie(key='session_id', value=user.id, expires=120, max_age=120, secure=False, httponly=True, samesite='None')
            return {'msg': 'OK. Completed!', 'session_id': user.id}
        # response.set_cookie(key='session_id', value=user.id, expires=120, max_age=120, secure=False, httponly=True, samesite='None')
        return {'msg': 'OK. Completed!', 'session_id': user.id}
    else:
        user = User()
        session.add(user)
        session.commit()
        session.refresh(user)
        # response.set_cookie(key='session_id', value=user.id, expires=120, max_age=120, secure=False, httponly=True, samesite='None')
        return {'msg': 'OK. Completed!', 'session_id': user.id}


@app.get('/api/videos_data')
async def root(session_id: str):
    session = retrieve_db_instance()

    if session_id not in exceptions:
        exceptions[session_id] = set()
    # videos = session.query(VideoData).filter(VideoData.video_id.notin_(exceptions[session_id])).order_by(VideoData.video_id.desc()).limit(10).all()
    # ids = set([video.video_id for video in videos])



    session_id = uuid.UUID(session_id)
    user = session.query(User).filter(User.id == session_id).first()


    ur = session.query(UserInteractions).filter(UserInteractions.user_id == session_id).all()
    ids = set([interaction.video_id for interaction in ur])
    df = pd.DataFrame(columns=['user_id', 'item_id', 'response'])
    for interaction in ur:
        df.loc[len(df)] = [str(interaction.user_id), interaction.video_id, int(interaction.liked)]

    df = score(rec, data=df, item_eligibility=exceptions)

    video_ids = set(df['item_id'].tolist())
    exceptions[session_id] = exceptions[session_id] | video_ids

    videos = session.query(VideoData).filter(VideoData.video_id.notin_(exceptions[session_id])).order_by(VideoData.video_id.desc()).all()

    return videos