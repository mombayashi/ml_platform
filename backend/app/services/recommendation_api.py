from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.services.rakuten_api import get_rakuten_api_items


def recommend_similar_items(keyword: str, top_n: int = 5):
    # 楽天APIから商品取得
    items = get_rakuten_api_items(keyword)
    if not items:
        return []

    # 商品説明文を抽出
    descriptions = [item["name"] for item in items]

    # TF-IDFでベクトル化
    vectorizer = TfidfVectorizer(max_features=5000)
    vectors = vectorizer.fit_transform(descriptions)

    # 類似度行列を計算
    similarity_matrix = cosine_similarity(vectors)

    # 1つ目の商品を基準に類似商品を抽出（例: 最初のアイテム）
    target_index = 0
    similarities = similarity_matrix[target_index]

    # 類似度の高い順にソート（自分自身を除外）
    similar_indices = similarities.argsort()[::-1][1:top_n+1]

    recommended_items = [items[i] for i in similar_indices]
    return recommended_items
