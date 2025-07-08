import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAKUTEN_APP_ID = os.getenv("RAKUTEN_APP_ID")

def get_rakuten__api_items(keyword: str, hits: int = 10):
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"  # ←最新に更新
    params = {
        "applicationId": RAKUTEN_APP_ID,
        "keyword": keyword,
        "hits": hits,
        "format": "json"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    items = [
        {
            "name": item["Item"]["itemName"],
            "url": item["Item"]["itemUrl"],
            "price": item["Item"]["itemPrice"],
            "shop": item["Item"]["shopName"]
        }
        for item in data.get("Items", [])
    ]

    return items
