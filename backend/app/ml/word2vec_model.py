from gensim.models import Word2Vec
import os


class Word2VecTrainer:
    def __init__(self, model_path="models/word2vec.model"):
        self.model_path = model_path
        self.model = None

    def train(self, tokenized_sentences: list[list[str]]):
        self.model = Word2Vec(
            sentences=tokenized_sentences,
            vector_size=100,
            window=5,
            min_count=2,
            workers=4,
        )
        self.model.save(self.model_path)

    def load(self):
        if os.path.exists(self.model_path):
            self.model = Word2Vec.load(self.model_path)
        else:
            raise FileNotFoundError("Word2Vec モデルが見つかりません。先に train を実行してください。")

    def get_vector(self, word: str):
        if self.model and word in self.model.wv:
            return self.model.wv[word]
        return None
