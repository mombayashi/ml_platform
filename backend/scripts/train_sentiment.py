import os
from app.ml.sentiment_model import SentimentModel


def train_and_save_model():
    texts = [
        "今日は嬉しいです",
        "とても悲しい",
        "最高の気分",
        "最悪な気分"
    ]
    labels = [1, 0, 1, 0]  # ポジティブ=1、ネガティブ=0

    # 保存先ディレクトリを確認してなければ作成
    model_dir = "models"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    model = SentimentModel()
    model.train(texts, labels)  # 学習＆保存

    print("モデルの学習と保存が完了しました。")


if __name__ == "__main__":
    train_and_save_model()
