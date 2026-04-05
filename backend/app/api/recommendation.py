from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from app.services.recommendation_api import recommend_similar_items
from db.database import get_db

router = APIRouter()


class RecommendRequest(BaseModel):
    keyword: str = Field(..., description="検索に使用するキーワード")
    top_n: int = Field(default=5, description="返す推薦件数")


@router.post("/")
def get_recommendations(
    request: RecommendRequest,
    db: Session = Depends(get_db),
):
    try:
        items = recommend_similar_items(request.keyword, db, request.top_n)
        return {"keyword": request.keyword, "results": items}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
