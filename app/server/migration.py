import pandas as pd
import numpy as np

from db import retrieve_db_instance, engine, Base
from models import VideoData, User, UserInteractions


import pandas as pd

Base.metadata.create_all(bind=engine)

session = retrieve_db_instance()



# def row_to_dict(row):
#     return {
#         'liked': False,
#         'disliked': False,
#         'video_id': row['video_id'],
#         'v_pub_datetime': row['v_pub_datetime'],
#         'v_total_comments': row['v_total_comments'],
#         'v_year_views': row['v_year_views'],
#         'v_month_views': row['v_month_views'],
#         'v_week_views': row['v_week_views'],
#         'v_day_views': row['v_day_views'],
#         'v_likes': row['v_likes'],
#         'v_dislikes': row['v_dislikes'],
#         'v_duration': row['v_duration'],
#         'v_cr_click_like_7_days': row['v_cr_click_like_7_days'],
#         'v_cr_click_dislike_7_days': row['v_cr_click_dislike_7_days'],
#         'v_cr_click_vtop_7_days': row['v_cr_click_vtop_7_days'],
#         'v_cr_click_long_view_7_days': row['v_cr_click_long_view_7_days'],
#         'v_cr_click_comment_7_days': row['v_cr_click_comment_7_days'],
#         'v_cr_click_like_30_days': row['v_cr_click_like_30_days'],
#         'v_cr_click_dislike_30_days': row['v_cr_click_dislike_30_days'],
#         'v_cr_click_vtop_30_days': row['v_cr_click_vtop_30_days'],
#         'v_cr_click_long_view_30_days': row['v_cr_click_long_view_30_days'],
#         'v_cr_click_comment_30_days': row['v_cr_click_comment_30_days'],
#         'v_cr_click_like_1_days': row['v_cr_click_like_1_days'],
#         'v_cr_click_dislike_1_days': row['v_cr_click_dislike_1_days'],
#         'v_cr_click_vtop_1_days': row['v_cr_click_vtop_1_days'],
#         'v_cr_click_long_view_1_days': row['v_cr_click_long_view_1_days'],
#         'v_cr_click_comment_1_days': row['v_cr_click_comment_1_days'],
#         'v_is_hidden': row['v_is_hidden'],
#         'v_is_deleted': row['v_is_deleted'],
#         'v_avg_watchtime_1_day': row['v_avg_watchtime_1_day'],
#         'v_avg_watchtime_7_day': row['v_avg_watchtime_7_day'],
#         'v_avg_watchtime_30_day': row['v_avg_watchtime_30_day'],
#         'v_frac_avg_watchtime_1_day_duration': row['v_frac_avg_watchtime_1_day_duration'],
#         'v_frac_avg_watchtime_7_day_duration': row['v_frac_avg_watchtime_7_day_duration'],
#         'v_frac_avg_watchtime_30_day_duration': row['v_frac_avg_watchtime_30_day_duration'],
#         'v_category_popularity_percent_7_days': row['v_category_popularity_percent_7_days'],
#         'v_category_popularity_percent_30_days': row['v_category_popularity_percent_30_days'],
#         'v_long_views_1_days': row['v_long_views_1_days'],
#         'v_long_views_7_days': row['v_long_views_7_days'],
#         'v_long_views_30_days': row['v_long_views_30_days'],
#         'row_number': row['row_number'],
#         'title': row['title'],
#         'description': row['description'],
#         'category_id': row['category_id'],
#         'author_id': row['author_id']
#     }


# def insert_video_row(session, row):
#     video_data = row_to_dict(row)

#     video = VideoData(**video_data)

#     session.add(video)
#     session.commit()

# df = pd.read_csv('./cut_df.csv')

# for index, row in df.iterrows():
#     insert_video_row(session, row)