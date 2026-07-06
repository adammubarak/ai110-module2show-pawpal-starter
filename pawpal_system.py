from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional, Tuple


@dataclass
class Task:
    title: str
    category: str
    due_time: str
    priority: str = "medium"
    completed: bool = False
    recurrence: str = "none"
    frequency: Optional[str] = None
    due_date: Optional[date] = None

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def is_due_today(self) -> bool:
        """Return True when the task is due today."""
        if self.due_date is not None:
            return self.due_date == date.today()
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

    def sort_by_time(self) -> List["Task"]:
        """Return tasks sorted by due time."""
        return sorted(self._get_tasks(), key=lambda task: task.due_time.lower())

    def sort_tasks(self) -> List["Task"]:
        """Return tasks sorted by due time."""
        return self.sort_by_time()

    def filter_tasks(self, pet_name: Optional[str] = None, completed: Optional[bool] = None) -> List["Task"]:
        """Return tasks filtered by pet name and completion status."""
        if self.owner is not None:
            filtered_tasks: List["Task"] = []
            for pet in self.owner.get_pets():
                if pet_name is not None and pet.name.lower() != pet_name.lower():
                    continue
                for task in pet.get_tasks():
                    if completed is None or task.completed is completed:
                        filtered_tasks.append(task)
            return filtered_tasks

        filtered_tasks = list(self.tasks)
        if completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed is completed]
        return filtered_tasks

    def get_today_tasks(self) -> List["Task"]:
        """Return tasks that are due today."""
        return [task for task in self._get_tasks() if task.is_due_today()]

    def detect_conflicts(self) -> List[str]:
        """Return readable warnings when two tasks share the same due time."""
        conflicts: List[str] = []
        tasks = self._get_tasks()
        for index, first_task in enumerate(tasks):
            for second_task in tasks[index + 1 :]:
                if first_task.due_time.lower() == second_task.due_time.lower():
                    conflicts.append(
                        f"Conflict: {first_task.title} and {second_task.title} both happen at {first_task.due_time}."
                    )
        return conflicts

    def generate_recurring_tasks(self) -> List["Task"]:
        """Create simple copies of recurring tasks for the next cycle."""
        recurring_tasks: List["Task"] = []
        for task in self._get_tasks():
            recurrence = (task.frequency or task.recurrence or "").strip().lower()
            if recurrence == "daily":
                next_date = (task.due_date or date.today()) + timedelta(days=1)
            elif recurrence == "weekly":
                next_date = (task.due_date or date.today()) + timedelta(days=7)
            else:
                continue

            recurring_tasks.append(
                Task(
                    title=task.title,
                    category=task.category,
                    due_time=task.due_time,
                    priority=task.priority,
                    completed=False,
                    recurrence=task.recurrence,
                    frequency=task.frequency,
                    due_date=next_date,
                )
            )
        return recurring_tasks
