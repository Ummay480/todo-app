"""Task data model and validation for Todo CLI Application"""

from typing import Literal, TypedDict, NotRequired
from datetime import datetime


# Type definitions
TaskStatus = Literal["pending", "completed"]


class Task(TypedDict):
    """Represents a todo task.

    Attributes:
        id: Unique identifier for the task
        title: Description of what needs to be done
        status: Current state of the task (pending or completed)
        category: Optional category for organization
        tags: Optional list of tags for flexible classification
        created_at: ISO timestamp of task creation
        updated_at: ISO timestamp of last modification
    """

    id: int
    title: str
    status: TaskStatus
    category: NotRequired[str | None]
    tags: NotRequired[list[str]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]


class TodoError(Exception):
    """Custom exception for Todo application errors"""

    pass


def is_valid_title(title: str) -> bool:
    """Validate task title according to FR-005.

    A valid title must:
    - Be a string
    - Contain at least one non-whitespace character
    - Be 1000 characters or less

    Args:
        title: The title string to validate

    Returns:
        True if title is valid, False otherwise

    Examples:
        >>> is_valid_title("Buy groceries")
        True
        >>> is_valid_title("")
        False
        >>> is_valid_title("   ")
        False
        >>> is_valid_title("a" * 1001)
        False
    """
    if not isinstance(title, str):
        return False
    if not title.strip():  # Catches empty and whitespace-only
        return False
    if len(title) > 1000:  # Edge case from spec
        return False
    return True


def get_timestamp() -> str:
    """Get current timestamp in ISO format.

    Returns:
        ISO formatted timestamp string
    """
    return datetime.now().isoformat()


def create_task(
    task_id: int,
    title: str,
    status: TaskStatus = "pending",
    category: str | None = None,
    tags: list[str] | None = None
) -> Task:
    """Create a new task with all fields.

    Args:
        task_id: Unique task identifier
        title: Task title
        status: Task status (default: pending)
        category: Optional category
        tags: Optional list of tags

    Returns:
        Complete Task dictionary
    """
    timestamp = get_timestamp()
    return {
        "id": task_id,
        "title": title,
        "status": status,
        "category": category,
        "tags": tags or [],
        "created_at": timestamp,
        "updated_at": timestamp
    }
