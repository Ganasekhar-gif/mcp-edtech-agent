def get_installation_context() -> dict:
    """
    Returns metadata about the current installation/deployment.
    This helps the assistant adapt to the capabilities of the current platform.

    Returns:
        dict: Dictionary representing platform-level settings and features.
    """
    return {
        "platformName": "Sunbird Ed - Pathshala",
        "availableContentTypes": ["video", "interactive", "document"],
        "enabledFeatures": ["course-recommendations", "progress-tracking"],
        "language": "en-IN",
        "branding": {
            "primaryColor": "#005FA3",
            "logoUrl": "https://example.com/logo.png"
        }
    }
