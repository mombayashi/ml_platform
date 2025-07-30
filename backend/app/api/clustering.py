from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from app.services.clustering_api import perform_clustering
from db.database import get_db

router = APIRouter()


class ClusteringRequest(BaseModel):
    data: List[List[float]]       # 特徴量
    item_codes: List[str]         # 商品コード
    n_clusters: int               # クラスタ数


@router.post("/")
def get_clusters(request: ClusteringRequest, db: Session = Depends(get_db)):
    try:
        clusters = perform_clustering(
            request.data,
            request.item_codes,
            request.n_clusters,
            db
        )
        return {"item_codes": request.item_codes, "clusters": clusters}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
