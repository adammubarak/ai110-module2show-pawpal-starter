from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class Task:
    title: str
    category: str
    due_time: str
    priority: str = "medium"
    completed: bool = False
    recurrence: str = "none"

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def is_due_today(self) -> bool:
        """Return True when the task is due today."""
        return self.due_time.strip().lower() in {"today", "today!"} or self.due_time.strip().lower().startswith("today")


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    notes: str = ""
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, task: "Task") -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List["Task"]:
        """Return all tasks for this pet."""
        return list(self.tasks)


@dataclass
class Owner:
    name: str
    email: str
    pets: List["Pet"] = field(default_factory=list)

    def add_pet(self, pet: "Pet") -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet from this owner by name."""
        self.pets = [pet for pet in self.pets if pet.name != pet_name]

    def get_pets(self) -> List["Pet"]:
        """Return all pets for this owner."""
        return list(self.pets)

    def get_all_tasks(self) -> List["Task"]:
        """Return all tasks from every pet owned by this owner."""
        all_tasks: List["Task"] = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


@dataclass
class Scheduler:
    owner: Optional["Owner"] = None
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, task: "Task") -> None:
        """Add a task to the scheduler."""
        self.tasks.append(task)

    def _get_tasks(self) -> List["Task"]:
        """Collect tasks from the owner when available, otherwise use the scheduler list."""
        if self.owner is not None:
            return self.owner.get_all_tasks()
        return list(self.tasks)

    def sort_tasks(self) -> List["Task"]:
        """Return tasks sorted by due time and priority."""
        priority_rank = {"low": 0, "medium": 1, "high": 2}
        return sorted(
            self._get_tasks(),
            key=lambda task: (
                task.due_time.lower(),
                -priority_rank.get(task.priority.lower(), 1),
            ),
        )

    def get_today_tasks(self) -> List["Task"]:
        """Return tasks that are due today."""
        return [task for task in self._get_tasks() if task.is_due_today()]

    def detect_conflicts(self) -> List[Tuple["Task", "Task"]]:
        """Return pairs of tasks that share the same due time."""
        conflicts: List[Tuple["Task", "Task"]] = []
        tasks = self._get_tasks()
        for index, first_task in enumerate(tasks):
            for second_task in tasks[index + 1 :]:
                if first_task.due_time.lower() == second_task.due_time.lower():
                    conflicts.append((first_task, second_task))
        return conflicts

    def generate_recurring_tasks(self) -> List["Task"]:
        """Create simple copies of recurring tasks."""
        recurring_tasks: List["Task"] = []
        for task in self._get_tasks():
            if task.recurrence.lower() != "none":
                recurring_tasks.append(
                    Task(
                        title=task.title,
                        category=task.category,
                        due_time=task.due_time,
                        priority=task.priority,
                        completed=False,
                        recurrence=task.recurrence,
                    )
                )
        return recurring_tasks
