import pandas as pd
from db import retrieve_db_instance
from models import User, UserInteractions, VideoData

from mab2rec import BanditRecommender, LearningPolicy, NeighborhoodPolicy
from mab2rec.pipeline import train, score
from mab2rec.utils import save_pickle, load_pickle
import os

pickle_path = os.path.join('.', 'rec.pkl')


rec = BanditRecommender(learning_policy=LearningPolicy.Popularity(), top_k=10)

train(
    rec,
    item_features='data/stats_sample50k.csv',
    data='data/ui_sample50k.csv',
    save_file=pickle_path
)

