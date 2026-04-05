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


def save_recommendations(
    db: Session,
    base_item_code: str,
    recommended_items: list[dict],
):
    results = []
    for item in recommended_items:
        rec = models.Recommendation(
            base_item_code=base_item_code,
            recommended_item_code=item.get("item_code", ""),
            similarity_score=item.get("similarity_score"),
        )
        db.add(rec)
        results.append(rec)
    db.commit()
    return results


def save_clusters(db: Session, item_codes: list[str], clusters: list[int]):
    results = []
    for item_code, cluster_id in zip(item_codes, clusters):
        cluster = models.Cluster(
            item_code=item_code,
            cluster_id=cluster_id
        )
        db.add(cluster)
        results.append(cluster)
    db.commit()
    return results
