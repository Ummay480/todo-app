"""In-memory storage for Todo tasks"""

from typing import List
from src.models.task import Task


class TaskStorage:
    """Manages in-memory storage of tasks.

    This class provides CRUD operations for tasks stored in a Python list.
    All operations are deterministic and suitable for single-session CLI use.
    """

    def __init__(self) -> None:
        """Initialize empty task storage with ID counter"""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def generate_id(self) -> int:
        """Generate next unique task ID.

        IDs are auto-incremented starting from 1, ensuring deterministic
        behavior across runs with the same operation sequence.

        Returns:
            Next available task ID
        """
        task_id = self._next_id
        self._next_id += 1
        return task_id

    def add_task(self, task: Task) -> None:
        """Add a task to storage.

        Args:
            task: Task dictionary with id, title, and status fields
        """
        self._tasks.append(task)

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks from storage.

        Returns:
            List of all tasks in storage
        """
        return self._tasks.copy()

    def has_duplicate(self, title: str) -> bool:
        """Check if a task with the given title already exists.

        Uses case-sensitive exact string matching for deterministic behavior.

        Args:
            title: Title to check for duplicates

        Returns:
            True if a task with this title exists, False otherwise
        """
        return any(task["title"] == title for task in self._tasks)
