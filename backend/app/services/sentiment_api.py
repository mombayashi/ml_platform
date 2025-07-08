from textblob import TextBlob

def analyze_sentiment(text: str) -> dict:
    """
    与えられたテキストの感情分析を行うサンプル関数。

    Args:
        text (str): 感情分析対象のテキスト

    Returns:
        dict: polarity（感情の極性：-1～1）、subjectivity（主観性：0～1）
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment

    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity
    }
