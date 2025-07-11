from app.ml.sentiment_model import SentimentModel

# モデルをグローバルにロード（起動時1回だけ読み込み）
model = SentimentModel()
model.load()

def predict_sentiment(text: str) -> dict:
    label = model.predict(text)
    label_map = {0: "negative", 1: "positive"}  # ラベルを意味のある文字列に変換
    return {"label": label_map.get(label, "unknown")}
