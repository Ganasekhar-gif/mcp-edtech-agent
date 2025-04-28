def load_installation_context() -> dict:
    """
    Loads installation-level context that helps the AI assistant
    understand deployment-specific data or configurations.

    This may include platform name, description, supported features, etc.

    Returns:
        dict: A dictionary representing the installation context.
    """
    context = {
        "platform_name": "Sunbird Ed - Local Deployment",  # Platform name for this deployment
        "organization": "COSS",  # Name of the organization hosting the platform
        "features": ["course_search", "user_enrollment", "progress_tracking"],  # Enabled features
        "support_email": "support@sunbirded.local",  # Support email for platform-related inquiries
        "branding": {
            "theme_color": "#004080",  # Primary theme color for the platform
            "logo_url": "https://example.com/logo.png"  # URL to the logo
        },
        "deployment_notes": "This is a local instance for demo/testing purposes."  # Additional notes
    }
    return context
