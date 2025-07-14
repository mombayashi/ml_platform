from sklearn.cluster import KMeans


def perform_clustering(data, n_clusters):
    """
    data: List[List[float]] - 多次元の数値データ
    n_clusters: int - クラスタ数

    Returns:
        List[int]: 各データ点のクラスタラベル
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    return kmeans.labels_.tolist()
