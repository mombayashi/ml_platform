from unittest.mock import patch, MagicMock
from app.services.sentiment_api import predict_sentiment


def test_predict_sentiment_positive():
    mock_model = MagicMock()
    mock_model.predict.return_value = 1

    with patch("app.services.sentiment_api.model", mock_model):
        result = predict_sentiment("最高の商品です")

    assert result["label"] == "positive"


def test_predict_sentiment_negative():
    mock_model = MagicMock()
    mock_model.predict.return_value = 0

    with patch("app.services.sentiment_api.model", mock_model):
        result = predict_sentiment("最悪な品質でした")

    assert result["label"] == "negative"


def test_predict_sentiment_returns_dict():
    mock_model = MagicMock()
    mock_model.predict.return_value = 1

    with patch("app.services.sentiment_api.model", mock_model):
        result = predict_sentiment("良い商品")

    assert isinstance(result, dict)
    assert "label" in result
