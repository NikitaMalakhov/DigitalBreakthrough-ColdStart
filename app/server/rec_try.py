import pandas as pd
from db import retrieve_db_instance
from models import User, UserInteractions, VideoData

from mab2rec import BanditRecommender, LearningPolicy, NeighborhoodPolicy
from mab2rec.pipeline import train, score
from mab2rec.utils import save_pickle, load_pickle
import os


rec = load_pickle(os.path.join('.', 'rec.pkl'))

