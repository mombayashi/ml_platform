from unittest.mock import MagicMock, patch
from app.services.clustering_api import perform_clustering


def test_clustering_returns_correct_count():
    data = [
        [1.0, 2.0],
        [1.5, 1.8],
        [5.0, 8.0],
        [8.0, 8.0],
    ]
    item_codes = ["A001", "A002", "A003", "A004"]
    db = MagicMock()

    with patch("app.services.clustering_api.save_clusters"):
        clusters = perform_clustering(data, item_codes, n_clusters=2, db=db)

    assert len(clusters) == len(item_codes)


def test_clustering_labels_within_range():
    data = [
        [1.0, 0.0],
        [0.0, 1.0],
        [10.0, 0.0],
        [0.0, 10.0],
    ]
    item_codes = ["X1", "X2", "X3", "X4"]
    db = MagicMock()
    n_clusters = 2

    with patch("app.services.clustering_api.save_clusters"):
        clusters = perform_clustering(data, item_codes, n_clusters=n_clusters, db=db)

    assert all(0 <= c < n_clusters for c in clusters)
