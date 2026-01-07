from typing import Dict, Any, Optional
from ..mcp_tools.list_tasks import list_tasks
from ..mcp_tools.get_task import get_task
from ..mcp_tools.update_task import update_task
from ..mcp_tools.delete_task import delete_task
from ..mcp_tools.toggle_complete import toggle_complete

class TaskManagerAgent:
    def list_tasks(self, context: Dict[str, Any]) -> str:
        return list_tasks(context=context)

    def get_task(self, message: str, context: Dict[str, Any]) -> str:
        # Dummy ID extraction
        task_id = 1
        return get_task(task_id=task_id, context=context)

    def update_task(self, message: str, context: Dict[str, Any]) -> str:
        task_id = 1
        title = "Updated Title from Chat"
        return update_task(task_id=task_id, title=title, context=context)

    def delete_task(self, message: str, context: Dict[str, Any]) -> str:
        task_id = 1
        return delete_task(task_id=task_id, context=context)

    def toggle_complete(self, message: str, context: Dict[str, Any]) -> str:
        task_id = 1
        return toggle_complete(task_id=task_id, context=context)