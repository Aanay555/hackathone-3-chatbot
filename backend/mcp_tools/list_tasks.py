import httpx
from typing import Optional, Dict, Any

def list_tasks(
    status: Optional[str] = None,
    keyword: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None
) -> str:
    """
    List tasks for the authenticated user with optional filtering.

    Args:
        status: Optional filter ("complete" or "incomplete")
        keyword: Optional search keyword in title/description
        context: Must contain 'jwt_token' and 'user_id'

    Returns:
        Formatted task list or friendly message.
    """
    if not context or "jwt_token" not in context or "user_id" not in context:
        return "Error: Authentication missing. Please log in to view your tasks."

    jwt_token = context["jwt_token"]
    user_id = context["user_id"]

    url = f"http://localhost:8000/api/{user_id}/tasks"
    params = {}
    if status:
        params["status"] = status.lower()
    if keyword:
        params["search"] = keyword

    headers = {"Authorization": f"Bearer {jwt_token}"}

    try:
        with httpx.Client() as client:
            response = client.get(url, params=params, headers=headers)

        if response.status_code == 401:
            return "Error: Session expired. Please log in again."

        if response.status_code != 200:
            return f"Error: Couldn't load tasks (code {response.status_code}). Try again later."

        tasks = response.json()

        if not tasks:
            return "You have no tasks yet! 🎯 Say 'Add a task to study Python' to create one."

        lines = ["Your Tasks 📋\n"]
        for i, task in enumerate(tasks, 1):
            title = task.get("title", "No title")
            task_id = task.get("id", "?")
            completed = task.get("completed", False)
            status_emoji = "✅ Complete" if completed else "⏳ Incomplete"
            due = task.get("due_date")
            due_str = f" | Due: {due}" if due else ""

            lines.append(f"{i}. ID: {task_id} | {title} | {status_emoji}{due_str}")

        lines.append(f"\nTotal: {len(tasks)} task{'s' if len(tasks) != 1 else ''}")

        return "\n".join(lines)

    except httpx.RequestError:
        return "Network error: Couldn't reach the server. Check your connection."

    except Exception as e:
        return f"Unexpected error: {str(e)}"