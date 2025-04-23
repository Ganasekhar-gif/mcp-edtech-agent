import requests
from configs.settings import BASE_URL


def get_learning_progress(user_id: str, course_id: str) -> dict:
    """
    Fetch learning progress for a user in a specific course.

    Args:
        user_id (str): Unique user ID.
        course_id (str): Unique course ID.

    Returns:
        dict: Progress data or error message.
    """
    try:
        url = f"{BASE_URL}/user/v1/profile"
        payload = {
            "request": {
                "userId": user_id,
                "courseId": course_id
            }
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
