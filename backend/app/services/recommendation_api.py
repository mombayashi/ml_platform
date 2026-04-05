from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy.orm import Session
from app.services.rakuten_api import get_rakuten_api_items
from db import crud


def recommend_similar_items(
    keyword: str,
    db: Session,
    top_n: int = 5,
):
    items = get_rakuten_api_items(keyword)
    if not items:
        return []

    descriptions = [item["name"] for item in items]

    vectorizer = TfidfVectorizer(max_features=5000)
    vectors = vectorizer.fit_transform(descriptions)

    similarity_matrix = cosine_similarity(vectors)

    target_index = 0
    similarities = similarity_matrix[target_index]

    similar_indices = similarities.argsort()[::-1][1:top_n + 1]

    recommended_items = []
    for i in similar_indices:
        item = dict(items[i])
        item["similarity_score"] = float(similarities[i])
        recommended_items.append(item)

    base_item_code = items[target_index].get("item_code", "")
    if base_item_code and db is not None:
        crud.save_recommendations(db, base_item_code, recommended_items)

    return recommended_items
