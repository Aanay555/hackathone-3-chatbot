import httpx
from typing import Optional, Dict, Any

def delete_task(
    task_id: int,
    context: Optional[Dict[str, Any]] = None
) -> str:
    """
    Permanently delete a task for the authenticated user.

    Args:
        task_id: The ID of the task to delete
        context: Must contain 'jwt_token' and 'user_id'

    Returns:
        Confirmation message or friendly error.
    """
    if not context or "jwt_token" not in context or "user_id" not in context:
        return "Error: Authentication missing. Please log in to delete tasks."

    jwt_token = context["jwt_token"]
    user_id = context["user_id"]

    url = f"http://localhost:8000/api/{user_id}/tasks/{task_id}"
    headers = {"Authorization": f"Bearer {jwt_token}"}

    try:
        with httpx.Client() as client:
            response = client.delete(url, headers=headers)

        if response.status_code == 404:
            return f"No task found with ID {task_id} in your list."

        if response.status_code == 401:
            return "Error: Session expired. Please log in again."

        if response.status_code == 204 or response.status_code == 200:
            return f"Task {task_id} has been permanently deleted. 🗑️"

        return f"Error deleting task (status {response.status_code}). Please try again."

    except httpx.RequestError:
        return "Network error: Could not reach server. Please try again later."

    except Exception as e:
        return f"Unexpected error: {str(e)}"