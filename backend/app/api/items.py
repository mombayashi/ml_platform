import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from app.services.rakuten_api import get_rakuten__api_items


router = APIRouter()

load_dotenv()

RAKUTEN_APP_ID = os.getenv("RAKUTEN_APP_ID")

@router.get("/")
def get_items(keyword: str, hits: int = 10):
    try:
        items = get_rakuten__api_items(keyword, hits)
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
