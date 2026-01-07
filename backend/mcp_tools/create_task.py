import httpx
from typing import Optional, Dict, Any
import json

def create_task(
    title: str,
    description: Optional[str] = None,
    due_date: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None
) -> str:
    """
    Creates a new task for the authenticated user via the FastAPI backend.

    Args:
        title: The title of the task (required).
        description: An optional description of the task.
        due_date: An optional due date for the task in YYYY-MM-DD format.
        context: Agent context containing the JWT token and user information.

    Returns:
        A friendly success message with the new task details,
        or an error message if the operation fails.
    """
    if not context or "jwt_token" not in context or "user_id" not in context:
        return "Error: Missing authentication context. Please ensure you are logged in."

    jwt_token = context["jwt_token"]
    user_id = context["user_id"]

    url = f"http://localhost:8000/api/{user_id}/tasks"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "title": title,
        "description": description,
        "due_date": due_date,
    }

    try:
        with httpx.Client() as client:
            response = client.post(url, headers=headers, json=payload)

        if response.status_code == 201:
            try:
                response_data = response.json()
                task_id = response_data.get("id")
                task_title = response_data.get("title")
                task_description = response_data.get("description")
                task_due_date = response_data.get("due_date")
                return (
                    f"Successfully created task! 🎉\n"
                    f"ID: {task_id}\n"
                    f"Title: {task_title}\n"
                    f"Description: {task_description or 'None'}\n"
                    f"Due Date: {task_due_date or 'Not set'}"
                )
            except json.JSONDecodeError:
                return "Task created successfully, but could not parse the details from the response."

        elif response.status_code == 400:
            error_detail = response.text
            return f"Error creating task: Bad request. Details: {error_detail}. Please check your input."

        elif response.status_code == 401:
            return "Error creating task: Unauthorized. Your session may have expired. Please log in again."

        elif response.status_code == 422:
            error_detail = response.text
            return f"Error creating task: Validation failed. Details: {error_detail}. Please check your input."

        else:
            return f"Error creating task: Server responded with status {response.status_code}. Please try again later."

    except httpx.RequestError as e:
        return f"Error creating task: A network error occurred - {e}. Please check your connection and try again."

    except Exception as e:
        return f"An unexpected error occurred while creating the task: {e}. Please try again."