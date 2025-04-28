from tools.course_metadata import search_courses
from tools.user_enrollment import get_user_enrollments
from tools.progress_tracker import get_learning_progress
from tools.learning_history import get_learning_history
from tools.preferred_content import get_preferred_content_types
from tools.installation_context import get_installation_context


def fetch_user_summary(user_id: str) -> dict:
    """
    Summarizes current course progress and personalization data for a user,
    enriched with installation-level context to adapt to platform capabilities.
    """
    summary_lines = []

    # 🛠️ Get platform-level configuration
    context = get_installation_context()
    platform_name = context.get("platformName", "this platform")
    enabled_features = context.get("enabledFeatures", [])
    supported_content = context.get("availableContentTypes", [])

    summary_lines.append(f"📡 Welcome to **{platform_name}**!")

    # 📘 Course Progress
    enrollments = get_user_enrollments(user_id)
    enrolled_courses = []
    if not enrollments or not enrollments.get("result", {}).get("courses"):
        summary_lines.append("You're not enrolled in any courses yet. Let's get started!")
    else:
        summary_lines.append("\n📘 Current Course Progress:")
        for enrollment in enrollments.get("result", {}).get("courses", []):
            course_id = enrollment.get("courseId")
            course_name = enrollment.get("courseName", "Unnamed Course")
            enrolled_courses.append(course_id)

            # Fetch learning progress for each course
            progress_data = get_learning_progress(user_id, course_id)
            progress_percent = 0
            if progress_data and "result" in progress_data:
                progress_list = progress_data["result"].get("progress", [])
                matched = next((p for p in progress_list if p.get("courseId") == course_id), None)
                if matched:
                    progress_percent = matched.get("completionPercentage", 0)

            summary_lines.append(f"- {course_name}: {progress_percent}% complete")

    # 🕘 Learning History
    history_data = get_learning_history(user_id)
    if history_data and "result" in history_data:
        history_courses = history_data["result"].get("accessLogs", [])
        if history_courses:
            summary_lines.append("\n🕘 Recently Accessed Courses:")
            for course in history_courses:
                course_name = course.get("courseName", "Unnamed Course")
                last_accessed = course.get("lastAccessed", "Unknown date")
                summary_lines.append(f"- {course_name} (Last accessed: {last_accessed})")

    # 🎯 Preferred Content Types
    preferred_types = {}
    content_pref_data = get_preferred_content_types(user_id)
    if content_pref_data and "result" in content_pref_data:
        preferences = content_pref_data["result"].get("preferences", {})
        if preferences:
            preferred_types = preferences
            summary_lines.append("\n🎯 Preferred Content Types:")
            for content_type, score in preferences.items():
                if content_type.lower() in supported_content:  # Check if platform supports it
                    summary_lines.append(f"- {content_type.capitalize()}: {score}%")

    # ✨ Recommendations (only if feature is enabled)
    if preferred_types and "course-recommendations" in enabled_features:
        top_preference = max(preferred_types.items(), key=lambda x: x[1])[0].lower()

        # Only search if the preferred type is supported by platform
        if top_preference in supported_content:
            search_result = search_courses(query=top_preference)

            # Fallback to popular if no specific content type results found
            if not search_result.get("result", {}).get("courses"):
                search_result = search_courses(query="popular")

            # Filter out already enrolled courses
            recommendations = []
            for course in search_result.get("result", {}).get("courses", []):
                if course["id"] not in enrolled_courses:
                    recommendations.append(f"- {course['name']}: {course.get('description', 'No description available')}")
                if len(recommendations) >= 3:
                    break

            if recommendations:
                summary_lines.append("\n✨ Recommended for You:")
                summary_lines.extend(recommendations)
            else:
                summary_lines.append("\n✨ No new course recommendations at the moment. Check back later!")

    summary_text = f"📊 Learning Summary for {user_id}:\n" + "\n".join(summary_lines)
    return {"result": summary_text}
