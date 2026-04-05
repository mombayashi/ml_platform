from unittest.mock import patch, MagicMock
from app.services.recommendation_api import recommend_similar_items

MOCK_ITEMS = [
    {"item_code": "A001", "name": "ワイヤレスイヤホン 高音質", "price": 5000, "url": "", "shop": ""},
    {"item_code": "A002", "name": "ワイヤレスイヤホン ノイズキャンセリング", "price": 8000, "url": "", "shop": ""},
    {"item_code": "A003", "name": "有線イヤホン 高音質", "price": 3000, "url": "", "shop": ""},
    {"item_code": "A004", "name": "スピーカー Bluetooth", "price": 10000, "url": "", "shop": ""},
    {"item_code": "A005", "name": "ヘッドホン 高音質 ワイヤレス", "price": 15000, "url": "", "shop": ""},
]


def test_recommend_returns_items():
    db = MagicMock()
    with patch("app.services.recommendation_api.get_rakuten_api_items", return_value=MOCK_ITEMS):
        with patch("app.services.recommendation_api.crud.save_recommendations"):
            result = recommend_similar_items("イヤホン", db, top_n=3)

    assert len(result) <= 3


def test_recommend_excludes_base_item():
    db = MagicMock()
    with patch("app.services.recommendation_api.get_rakuten_api_items", return_value=MOCK_ITEMS):
        with patch("app.services.recommendation_api.crud.save_recommendations"):
            result = recommend_similar_items("イヤホン", db, top_n=4)

    item_codes = [item["item_code"] for item in result]
    assert "A001" not in item_codes


def test_recommend_includes_similarity_score():
    db = MagicMock()
    with patch("app.services.recommendation_api.get_rakuten_api_items", return_value=MOCK_ITEMS):
        with patch("app.services.recommendation_api.crud.save_recommendations"):
            result = recommend_similar_items("イヤホン", db, top_n=3)

    for item in result:
        assert "similarity_score" in item
        assert isinstance(item["similarity_score"], float)


def test_recommend_returns_empty_on_no_items():
    db = MagicMock()
    with patch("app.services.recommendation_api.get_rakuten_api_items", return_value=[]):
        result = recommend_similar_items("存在しないキーワード", db)

    assert result == []
