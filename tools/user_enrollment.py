import requests
from configs.settings import BASE_URL


def get_user_enrollments(user_id: str) -> dict:
    """
    Fetch enrollment data for a specific user.

    Args:
        user_id (str): Unique ID of the user.

    Returns:
        dict: Enrollment data or error message.
    """
    try:
        url = f"{BASE_URL}/user/enrollment/list"
        payload = {
            "request": {
                "userId": user_id
            }
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
