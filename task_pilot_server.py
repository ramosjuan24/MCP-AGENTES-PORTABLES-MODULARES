**Server-side task management with MCP**

from pathlib import Path
from typing import Optional, Dict
from uudid import uuid4
import json

from pydantic import BaseModel, Field
from mcp.server.fastmcp import FastMCP, Context

DATA_FILE = Path("data/tasks_data.json")
DATA_FILE.parent.mkdir(exist_ok=True)

def load_data() -> Dict[str, dict]:
    if DATA_FILE.exists():
       return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return {}

def load_data_by_id(task_id: str) -> Optional[dict]:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8")).get(task_id)
    return{}


def save_data(data: Dict[str, dict]) -> None:
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")  


    #--------------Data Models--------------#
class Task(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    title: str
    done: bool = False
    tags: list[str] = []
    

# Resolve any forward references (save even if none exist)

Task.model_rebuild()

STORE: Dict[str, dict] = load_data()

#--------------MCP Server Setup--------------#
mcp = FastMCP("Task Pilot Server")

#--------------MCP Tools--------------#
@mcp.tool()
def add_task(title: str, tags: Optional[list[str]] = None) -> Task:
    """Create and persist a new task"""
    title = (title or "").strip()
    if not title:
        raise ValueError("Title cannot be empty.")
    task = Task(title=title, tags=[t for t in (tags or []) if t.strip()])
    STORE[task.id] = task.model_dump()
    save_data(STORE)
    return task



@mcp.tool()
def create_task(title: str, context: Context) -> Task:
    """Create a new task with the given title."""
    task = Task(title=title)
    STORE[task.id] = task.model_dump()
    save_data(STORE)
    return task


