from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .db import Base
import uuid

class VideoData(Base):
    __tablename__ = 'video_data'
    liked = Column(Boolean, nullable=False)
    disliked = Column(Boolean, nullable=False)
    video_id = Column(String, primary_key=True, nullable=False)
    v_pub_datetime = Column(String, nullable=False)
    v_total_comments = Column(Integer, nullable=False)
    v_year_views = Column(Integer, nullable=False)
    v_month_views = Column(Integer, nullable=False)
    v_week_views = Column(Integer, nullable=False)
    v_day_views = Column(Integer, nullable=False)
    v_likes = Column(Integer, nullable=False)
    v_dislikes = Column(Integer, nullable=False)
    v_duration = Column(Integer, nullable=False)
    v_cr_click_like_7_days = Column(Integer, nullable=False)
    v_cr_click_dislike_7_days = Column(Integer, nullable=False)
    v_cr_click_vtop_7_days = Column(Integer, nullable=False)
    v_cr_click_long_view_7_days = Column(Integer, nullable=False)
    v_cr_click_comment_7_days = Column(Integer, nullable=False)
    v_cr_click_like_30_days = Column(Integer, nullable=False)
    v_cr_click_dislike_30_days = Column(Integer, nullable=False)
    v_cr_click_vtop_30_days = Column(Integer, nullable=False)
    v_cr_click_long_view_30_days = Column(Integer, nullable=False)
    v_cr_click_comment_30_days = Column(Integer, nullable=False)
    v_cr_click_like_1_days = Column(Integer, nullable=False)
    v_cr_click_dislike_1_days = Column(Integer, nullable=False)
    v_cr_click_vtop_1_days = Column(Integer, nullable=False)
    v_cr_click_long_view_1_days = Column(Integer, nullable=False)
    v_cr_click_comment_1_days = Column(Integer, nullable=False)
    v_is_hidden = Column(Integer, nullable=False)
    v_is_deleted = Column(Integer, nullable=False)
    v_avg_watchtime_1_day = Column(Float, nullable=False)
    v_avg_watchtime_7_day = Column(Float, nullable=False)
    v_avg_watchtime_30_day = Column(Float, nullable=False)
    v_frac_avg_watchtime_1_day_duration = Column(Float, nullable=False)
    v_frac_avg_watchtime_7_day_duration = Column(Float, nullable=False)
    v_frac_avg_watchtime_30_day_duration = Column(Float, nullable=False)
    v_category_popularity_percent_7_days = Column(Float, nullable=False)
    v_category_popularity_percent_30_days = Column(Float, nullable=False)
    v_long_views_1_days = Column(Integer, nullable=False)
    v_long_views_7_days = Column(Integer, nullable=False)
    v_long_views_30_days = Column(Integer, nullable=False)
    row_number = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(String, nullable=False)
    author_id = Column(String, nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class UserInteractions(Base):
    __tablename__ = 'user_interactions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True))
    video_id = Column(String, nullable=False)
    liked = Column(Boolean, default=False)
    disliked = Column(Boolean, default=False)
