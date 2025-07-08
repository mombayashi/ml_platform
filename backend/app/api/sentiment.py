from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.sentiment_api import analyze_sentiment

router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

@router.post("/")
def get_sentiment(request: SentimentRequest):
    try:
        result = analyze_sentiment(request.text)
        return {"text": request.text, "sentiment": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
