import httpx
from typing import Optional, Dict, Any

def get_task(
    task_id: int,
    context: Optional[Dict[str, Any]] = None
) -> str:
    """
    Retrieve details of a specific task by ID for the authenticated user.

    Args:
        task_id: The ID of the task to retrieve
        context: Must contain 'jwt_token' and 'user_id' for authentication

    Returns:
        Formatted task details or friendly error message.
    """
    if not context or "jwt_token" not in context or "user_id" not in context:
        return "Error: Authentication missing. Please log in to view task details."

    jwt_token = context["jwt_token"]
    user_id = context["user_id"]

    url = f"http://localhost:8000/api/{user_id}/tasks/{task_id}"
    headers = {"Authorization": f"Bearer {jwt_token}"}

    try:
        with httpx.Client() as client:
            response = client.get(url, headers=headers)

        if response.status_code == 404:
            return f"I couldn't find a task with ID {task_id} in your list. Please check the ID and try again."

        if response.status_code == 401:
            return "Error: Session expired. Please log in again."

        if response.status_code != 200:
            return f"Error: Could not retrieve task (status {response.status_code}). Please try again."

        task = response.json()

        title = task.get("title", "No title")
        description = task.get("description") or "No description"
        completed = task.get("completed", False)
        status_emoji = "✅ Complete" if completed else "⏳ Incomplete"
        due = task.get("due_date")
        due_str = f"Due Date: {due}" if due else "No due date"

        return (
            f"Task Details 🔍\n\n"
            f"ID: {task_id}\n"
            f"Title: {title}\n"
            f"Description: {description}\n"
            f"Status: {status_emoji}\n"
            f"{due_str}"
        )

    except httpx.RequestError:
        return "Network error: Couldn't connect to the server. Please try again later."

    except Exception as e:
        return f"Unexpected error occurred: {str(e)}"