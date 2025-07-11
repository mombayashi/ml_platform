import joblib
import os
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

class ClusteringModel:
    def __init__(self, model_path="models/clustering_model.pkl", vec_path="models/clustering_tfidf.pkl"):
        self.model_path = model_path
        self.vec_path = vec_path
        self.model = None
        self.vectorizer = None

    def train(self, texts: list[str], n_clusters: int = 5):
        self.vectorizer = TfidfVectorizer(max_features=1000)
        X = self.vectorizer.fit_transform(texts)

        self.model = KMeans(n_clusters=n_clusters)
        self.model.fit(X)

        joblib.dump(self.model, self.model_path)
        joblib.dump(self.vectorizer, self.vec_path)

    def load(self):
        if os.path.exists(self.model_path) and os.path.exists(self.vec_path):
            self.model = joblib.load(self.model_path)
            self.vectorizer = joblib.load(self.vec_path)
        else:
            raise FileNotFoundError("クラスタリングモデルまたはベクトライザが見つかりません")

    def predict_cluster(self, text: str) -> int:
        X = self.vectorizer.transform([text])
        return int(self.model.predict(X)[0])
