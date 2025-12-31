"""Task data model and validation for Todo CLI Application"""

from typing import Literal, TypedDict


# Type definitions
TaskStatus = Literal["pending", "completed"]


class Task(TypedDict):
    """Represents a todo task.

    Attributes:
        id: Unique identifier for the task
        title: Description of what needs to be done
        status: Current state of the task (pending or completed)
    """

    id: int
    title: str
    status: TaskStatus


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
