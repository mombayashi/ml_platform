from sklearn.cluster import KMeans
from sqlalchemy.orm import Session
from db.crud import save_clusters


def perform_clustering(
    data: list[list[float]],
    item_codes: list[str],
    n_clusters: int,
    db: Session
) -> list[int]:
    """
    data: List[List[float]] - クラスタリングする特徴量
    item_codes: List[str] - 各データに対応する商品コード
    n_clusters: int
    db: Session
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    clusters = kmeans.labels_.tolist()

    # DBに保存
    save_clusters(db, item_codes, clusters)
    return clusters
