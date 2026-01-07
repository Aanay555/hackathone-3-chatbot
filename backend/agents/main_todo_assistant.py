from openai import OpenAI
from mcp_tools.create_task import create_task
from mcp_tools.list_tasks import list_tasks
from mcp_tools.get_task import get_task
from mcp_tools.update_task import update_task
from mcp_tools.delete_task import delete_task
from mcp_tools.toggle_complete import toggle_complete

client = OpenAI()

def todo_assistant(message: str, context: dict) -> str:
    """
    Main Todo Assistant - understands natural language and delegates to sub-tools.
    """
    messages = [
        {"role": "system", "content": """
You are TodoAssistant, an intelligent personal task manager.
You help users manage their todo list using natural language.
You have access to tools for creating, listing, viewing, updating, deleting, and marking tasks.

Rules:
- Always be friendly, concise, and helpful.
- Confirm actions when possible (e.g., "Task created!", "Marked as complete!").
- If unclear, ask for clarification.
- Never expose other users' data.
- Use the available tools only when needed.
        """},
        {"role": "user", "content": message}
    ]

    tools = [
        {
            "type": "function",
            "function": {
                "name": "create_task",
                "description": "Create a new task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "due_date": {"type": "string"}
                    },
                    "required": ["title"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "list_tasks",
                "description": "List all tasks with optional filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string", "enum": ["complete", "incomplete"]},
                        "keyword": {"type": "string"}
                    }
                }
            }
        },
        # Add other tools similarly: get_task, update_task, delete_task, toggle_complete
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    # Handle tool calls (simplified — in real MCP, this is handled by SDK)
    # For now, we simulate direct tool execution
    # In full MCP SDK, this would be automatic

    # This is a simplified version for hackathon demo
    # In production, use Official MCP SDK for proper delegation

    lower_msg = message.lower()

    if "add" in lower_msg or "create" in lower_msg or "new task" in lower_msg:
        return create_task(title="New Task from chat", context=context)
    elif "list" in lower_msg or "show" in lower_msg or "tasks" in lower_msg:
        return list_tasks(context=context)
    elif "delete" in lower_msg:
        return delete_task(task_id=1, context=context)  # In real: parse ID
    elif "complete" in lower_msg or "done" in lower_msg:
        return toggle_complete(task_id=1, context=context)
    else:
        return "I can help you add, list, update, delete, or mark tasks as complete. What would you like to do?"