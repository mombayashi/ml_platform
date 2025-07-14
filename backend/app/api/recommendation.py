from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.rakuten_api import get_rakuten__api_items

router = APIRouter()


class RecommendRequest(BaseModel):
    keyword: str = Field(..., description="検索に使用するキーワード")


@router.post("/")
def get_recommendations(request: RecommendRequest):
    try:
        items = get_rakuten__api_items(request.keyword)
        return {"keyword": request.keyword, "results": items}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
