def get_preferred_content_types(user_id: str) -> dict:
    """
    Returns mock data of user's preferred content types.

    In the future, this can be replaced with a real API call to fetch user preferences.
    """

    # Mock data (can be updated with real data later)
    mock_data = {
        "user123": {
            "result": {
                "preferences": {
                    "video": 65,
                    "interactive": 20,
                    "document": 10,
                    "project": 5
                }
            }
        },
        "user456": {
            "result": {
                "preferences": {
                    "interactive": 50,
                    "video": 30,
                    "document": 15,
                    "project": 5
                }
            }
        }
    }

    # For now, return the mock data
    if user_id in mock_data:
        return mock_data[user_id]
    else:
        return {"result": {"preferences": {}}}
