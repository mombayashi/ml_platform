import joblib
import os
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer


class SentimentModel:
    def __init__(
        self,
        model_path="models/sentiment_model.pkl",
        vec_path="models/tfidf.pkl",
    ):
        self.model_path = model_path
        self.vec_path = vec_path
        self.model = None
        self.vectorizer = None

    def train(self, texts: list[str], labels: list[int]):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        X = self.vectorizer.fit_transform(texts)

        self.model = LogisticRegression()
        self.model.fit(X, labels)

        joblib.dump(self.model, self.model_path)
        joblib.dump(self.vectorizer, self.vec_path)

    def load(self):
        if os.path.exists(self.model_path) and os.path.exists(self.vec_path):
            self.model = joblib.load(self.model_path)
            self.vectorizer = joblib.load(self.vec_path)
        else:
            raise FileNotFoundError("モデルまたはベクトライザが見つかりません")

    def predict(self, text: str) -> int:
        X = self.vectorizer.transform([text])
        return int(self.model.predict(X)[0])
