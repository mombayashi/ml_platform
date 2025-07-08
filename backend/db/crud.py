from sqlalchemy.orm import Session
from . import models


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: dict):
    db_item = models.Item(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
