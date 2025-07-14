from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_code = Column(String(255), unique=True, index=True, nullable=False)
    item_name = Column(String(512))
    item_caption = Column(Text)
    price = Column(Integer)
    genre_id = Column(String(50))
    review_average = Column(Float)
    review_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    item_code = Column(String(255), index=True, nullable=False)
    review_text = Column(Text)
    reviewer_name = Column(String(255))
    review_score = Column(Float)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    base_item_code = Column(String(255), index=True, nullable=False)
    recommended_item_code = Column(String(255), nullable=False)
    similarity_score = Column(Float)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))


class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True, index=True)
    review_id = Column(Integer, nullable=False)
    sentiment_label = Column(String(10))
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))


class PriceForecast(Base):
    __tablename__ = "price_forecasts"

    id = Column(Integer, primary_key=True, index=True)
    item_code = Column(String(255), index=True, nullable=False)
    forecast_date = Column(Date)
    predicted_price = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))


class Cluster(Base):
    __tablename__ = "clusters"

    id = Column(Integer, primary_key=True, index=True)
    item_code = Column(String(255), index=True, nullable=False)
    cluster_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
