import requests
import os
import re
from context.installation_context import load_installation_context
from configs.settings import MCP_API_BASE, MCP_MODEL
from tools.course_metadata import search_courses
from tools.user_enrollment import get_user_enrollments
from tools.progress_tracker import get_learning_progress
from tools.personalization_tool import fetch_user_summary


def extract_user_id_from_prompt(prompt: str) -> str:
    """
    Basic function to extract user ID from prompt. Assumes format like 'user id is user123' or 'user456'.
    If not found, defaults to 'user123'.
    """
    match = re.search(r'\buser(\d+)\b', prompt.lower())  # Look for patterns like user123, user456
    return match.group(0) if match else "user123"  # Return matched user or fallback to user123


def call_llama3(prompt: str, tools: list = None) -> str:
    """
    Handles prompt and optionally calls Sunbird Ed tools or the LLM depending on content.
    """
    context = load_installation_context()

    system_prompt = (
        f"You are a helpful AI assistant deployed on '{context['platform_name']}' by {context['organization']}.\n"
        f"Features available: {', '.join(context['features'])}.\n"
        f"Deployment note: {context['deployment_notes']}\n"
        f"Support contact: {context['support_email']}\n"
    )

    # Course search
    if "available courses" in prompt.lower() or "what courses" in prompt.lower():
        courses_response = search_courses(query="")
        if "courses" in courses_response.get('result', {}):
            courses = courses_response['result']['courses']
            course_names = [course['name'] for course in courses]
            return f"Here are the available courses: {', '.join(course_names)} on the Sunbird Ed platform."
        else:
            return "Sorry, I couldn't fetch the available courses right now."

    # User enrollment
    elif "enrollment" in prompt.lower() or "enrolled" in prompt.lower():
        user_id = extract_user_id_from_prompt(prompt)
        enrollment_response = get_user_enrollments(user_id)
        if "courses" in enrollment_response.get('result', {}):
            courses = enrollment_response['result']['courses']
            if not courses:
                return f"No enrollments found for user '{user_id}'."
            course_names = [course['courseName'] for course in courses]
            return f"User '{user_id}' is enrolled in: {', '.join(course_names)}."
        else:
            return f"Could not retrieve enrollment info for user '{user_id}'."

    # User progress
    elif "progress" in prompt.lower() or "profile" in prompt.lower():
        user_id = extract_user_id_from_prompt(prompt)
        enrollment_response = get_user_enrollments(user_id)

        if "courses" in enrollment_response.get('result', {}):
            progress_reports = []
            for course in enrollment_response['result']['courses']:
                course_id = course['courseId']
                course_name = course['courseName']
                progress_response = get_learning_progress(user_id, course_id)
                if "progress" in progress_response.get('result', {}):
                    progress_data = progress_response['result']['progress']
                    if isinstance(progress_data, list) and progress_data:
                        matched = next((p for p in progress_data if p.get('courseId') == course_id), None)
                        if matched:
                            percentage = matched.get('completionPercentage', 0)
                            progress_reports.append(f"{course_name}: {percentage}% complete")
                        else:
                            progress_reports.append(f"{course_name}: Progress not found in response.")
                    else:
                        progress_reports.append(f"{course_name}: No progress data available.")
                else:
                    progress_reports.append(f"{course_name}: Could not retrieve progress.")
            return f"Progress for user '{user_id}':\n" + "\n".join(progress_reports)
        else:
            return f"Could not retrieve enrolled courses to check progress for user '{user_id}'."

    # User summary (overview)
    elif "summary" in prompt.lower() or "overview" in prompt.lower():
        user_id = extract_user_id_from_prompt(prompt)
        try:
            summary_result = fetch_user_summary(user_id)
            return summary_result.get("result", "Could not generate summary.")

        except Exception as e:
            return f"[Summary Error] {str(e)}"

    # Fallback to LLM
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    try:
        response = requests.post(
            f"{MCP_API_BASE}/chat/completions",
            json={
                "model": MCP_MODEL,
                "messages": messages,
                "temperature": 0.7
            },
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[LLM Error] {str(e)}"
