import requests
from configs.settings import BASE_URL


def search_courses(query: str = "") -> dict:
    """
    Searches for courses using the Sunbird Ed API.

    Parameters:
        query (str): Optional keyword to search for specific courses.

    Returns:
        dict: Course search results or error message.
    """
    url = f"{BASE_URL}/course/v1/search"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "request": {
            "filters": {},
            "query": query,
            "limit": 10
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
