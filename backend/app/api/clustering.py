from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.clustering_api import perform_clustering

router = APIRouter()


class ClusteringRequest(BaseModel):
    data: List[List[float]]  # 多次元データのリスト
    n_clusters: int  # クラスタ数


@router.post("/")
def get_clusters(request: ClusteringRequest):
    try:
        clusters = perform_clustering(request.data, request.n_clusters)
        return {"data": request.data, "clusters": clusters}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
