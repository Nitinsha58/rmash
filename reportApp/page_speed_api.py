import requests
import json
from django.conf import settings

CLIENT_ID = settings.CLIENT_ID
CLIENT_SECRET = settings.CLIENT_SECRET
API_KEY = settings.API_KEY

def filterPageSpeedData(data=None):
    categories_data = {}
    audits_data = {}
    categories = data["lighthouseResult"]["categories"]
    audits = data["lighthouseResult"]["audits"]

    for field in categories:
        categories_data[field] = {
                "title" : categories[field]["title"],
                "score" : categories[field]["score"],
            }

    for field in ['uses-responsive-images', 'layout-shift-elements', 'lcp-lazy-loaded', 'timing-budget', 'http-status-code', 'largest-contentful-paint', 'cumulative-layout-shift', 'full-page-screenshot', 'robots-txt', 'image-alt']:
        audits_data[field] = {
            "id" : audits[field]["id"],
            "title" : audits[field]["title"],
            "score" : audits[field]["score"],
            "scoreDisplayMode" : audits[field]["scoreDisplayMode"],
        }
    filteredData = {
        "id": data["id"],
        "initial_url": data["loadingExperience"]["initial_url"],
        "formFactor": data["lighthouseResult"]["configSettings"]["formFactor"],
        "audits": audits_data,
        "categories": categories_data
    }

    return filteredData


def get_data(search_url = None):
    url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": search_url,
        "strategy": "mobile",
        "key": API_KEY,
        "category": ["performance", "seo", "accessibility", "best-practices", "pwa"]
    }

    res = requests.get(url, params=params)
    
    data = json.loads(res.text)
    return filterPageSpeedData(data)