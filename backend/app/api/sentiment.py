from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.services.sentiment_api import predict_sentiment
from db.database import get_db
from db import crud

router = APIRouter()

class SentimentRequest(BaseModel):
    review_id: int
    text: str = Field(..., description="感情分析を行いたいテキスト")

@router.post("/")
def get_sentiment(request: SentimentRequest, db: Session = Depends(get_db)):
    try:
        result = predict_sentiment(request.text)
        label = result["label"]
        confidence = result.get("confidence", 1.0)  # 未使用なら 1.0 固定でもOK

        # DBへ保存
        crud.save_sentiment(
            db=db,
            review_id=request.review_id,
            label=label,
            confidence=confidence
        )

        return {"review_id": request.review_id, "text": request.text, "sentiment": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
