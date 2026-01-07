from typing import Dict, Any
from ..mcp_tools.create_task import create_task

class TaskCreatorAgent:
    def handle(self, message: str, context: Dict[str, Any]) -> str:
        # Simple parsing (in real project, use LLM to extract title/description/due_date)
        # For demo, we use dummy values
        title = "New Task from Chat"
        description = message
        due_date = None

        return create_task(title=title, description=description, due_date=due_date, context=context)