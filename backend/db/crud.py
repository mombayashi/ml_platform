from sqlalchemy.orm import Session
from . import models
from datetime import datetime

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: dict):
    db_item = models.Item(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def save_sentiment(db: Session, review_id: int, label: str, confidence: float):
    db_sentiment = models.Sentiment(
        review_id=review_id,
        sentiment_label=label,
        confidence=confidence,
        created_at=datetime.utcnow()
    )
    db.add(db_sentiment)
    db.commit()
    db.refresh(db_sentiment)
    return db_sentiment
