def load_installation_context() -> dict:
    """
    Loads installation-level context that helps the AI assistant
    understand deployment-specific data or configurations.
    
    This may include platform name, description, supported features, etc.

    Returns:
        dict: A dictionary representing the installation context.
    """
    context = {
        "platform_name": "Sunbird Ed - Local Deployment",
        "organization": "COSS",
        "features": ["course_search", "user_enrollment", "progress_tracking"],
        "support_email": "support@sunbirded.local",
        "branding": {
            "theme_color": "#004080",
            "logo_url": "https://example.com/logo.png"
        },
        "deployment_notes": "This is a local instance for demo/testing purposes."
    }
    return context
