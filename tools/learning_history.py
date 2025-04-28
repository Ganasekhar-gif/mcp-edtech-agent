def get_learning_history(user_id: str) -> dict:
    """
    Returns mock learning history data based on user ID.

    In the future, this can be replaced with real API calls to fetch learning history.
    """

    # Mock data (can be updated with real data later)
    mock_data = {
        "user123": {
            "result": {
                "accessLogs": [
                    {"courseId": "python-101", "courseName": "Python Basics", "lastAccessed": "2025-04-21T13:00:00Z"},
                    {"courseId": "ds-101", "courseName": "Data Science 101", "lastAccessed": "2025-04-19T16:45:00Z"},
                    {"courseId": "sql-101", "courseName": "SQL Foundations", "lastAccessed": "2025-04-17T11:10:00Z"}
                ]
            }
        },
        "user456": {
            "result": {
                "accessLogs": [
                    {"courseId": "ai-300", "courseName": "Advanced AI", "lastAccessed": "2025-04-23T15:00:00Z"},
                    {"courseId": "ml-101", "courseName": "Machine Learning Intro",
                     "lastAccessed": "2025-04-22T10:30:00Z"}
                ]
            }
        }
    }

    # For now, return the mock data
    if user_id in mock_data:
        return mock_data[user_id]
    else:
        return {"result": {"accessLogs": []}}

