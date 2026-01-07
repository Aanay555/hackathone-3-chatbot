import httpx
from typing import Optional, Dict, Any

def toggle_complete(
    task_id: int,
    context: Optional[Dict[str, Any]] = None
) -> str:
    """
    Toggle the completion status of a task (complete ↔ incomplete).

    Args:
        task_id: The ID of the task to toggle
        context: Must contain 'jwt_token' and 'user_id'

    Returns:
        Confirmation with new status or friendly error.
    """
    if not context or "jwt_token" not in context or "user_id" not in context:
        return "Error: Authentication missing. Please log in to update tasks."

    jwt_token = context["jwt_token"]
    user_id = context["user_id"]

    url = f"http://localhost:8000/api/{user_id}/tasks/{task_id}/complete"
    headers = {"Authorization": f"Bearer {jwt_token}"}

    try:
        with httpx.Client() as client:
            response = client.patch(url, headers=headers)

        if response.status_code == 404:
            return f"No task found with ID {task_id} in your list."

        if response.status_code == 401:
            return "Error: Session expired. Please log in again."

        if response.status_code != 200:
            return f"Error toggling task (status {response.status_code}). Please try again."

        updated_task = response.json()
        completed = updated_task.get("completed", False)
        new_status = "Complete ✅" if completed else "Incomplete ⏳"
        title = updated_task.get("title", "the task")

        return f"Task {task_id} ('{title}') is now marked as {new_status}!"

    except httpx.RequestError:
        return "Network error: Could not reach server. Please try again later."

    except Exception as e:
        return f"Unexpected error: {str(e)}"