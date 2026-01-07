import httpx
from typing import Optional, Dict, Any

def update_task(
    task_id: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    due_date: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None
) -> str:
    """
    Update an existing task (partial updates allowed) for the authenticated user.

    Args:
        task_id: ID of the task to update
        title: New title (optional)
        description: New description (optional)
        due_date: New due date in YYYY-MM-DD format (optional)
        context: Must contain 'jwt_token' and 'user_id'

    Returns:
        Success message with updated fields or friendly error.
    """
    if not context or "jwt_token" not in context or "user_id" not in context:
        return "Error: Authentication missing. Please log in to update tasks."

    jwt_token = context["jwt_token"]
    user_id = context["user_id"]

    # Build payload only with provided fields
    payload = {}
    if title is not None:
        payload["title"] = title
    if description is not None:
        payload["description"] = description
    if due_date is not None:
        payload["due_date"] = due_date

    if not payload:
        return "No changes provided. Please specify what you'd like to update."

    url = f"http://localhost:8000/api/{user_id}/tasks/{task_id}"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }

    try:
        with httpx.Client() as client:
            response = client.put(url, json=payload, headers=headers)

        if response.status_code == 404:
            return f"Task with ID {task_id} not found in your list."

        if response.status_code == 401:
            return "Error: Session expired. Please log in again."

        if response.status_code == 422:
            return "Error: Invalid data provided. Please check your input."

        if response.status_code != 200:
            return f"Error updating task (status {response.status_code}). Please try again."

        updated_task = response.json()
        changes = []
        if title is not None:
            changes.append(f"Title → {updated_task.get('title')}")
        if description is not None:
            changes.append(f"Description → {updated_task.get('description') or 'None'}")
        if due_date is not None:
            changes.append(f"Due Date → {updated_task.get('due_date') or 'Not set'}")

        return (
            f"Task {task_id} updated successfully! ✅\n"
            + "\n".join(changes)
        )

    except httpx.RequestError:
        return "Network error: Could not reach server. Please try again."

    except Exception as e:
        return f"Unexpected error: {str(e)}"