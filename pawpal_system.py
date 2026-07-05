from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Owner:
    name: str
    email: str
    pets: List["Pet"] = field(default_factory=list)

    def add_pet(self, pet: "Pet") -> None:
        pass

    def remove_pet(self, pet: "Pet") -> None:
        pass

    def get_pets(self) -> List["Pet"]:
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    notes: str = ""
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, task: "Task") -> None:
        pass

    def get_tasks(self) -> List["Task"]:
        pass


@dataclass
class Task:
    title: str
    category: str
    due_time: str
    priority: str = "medium"
    completed: bool = False
    recurrence: str = "none"

    def mark_complete(self) -> None:
        pass

    def is_due_today(self) -> bool:
        pass


@dataclass
class Scheduler:
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, task: "Task") -> None:
        pass

    def sort_tasks(self) -> List["Task"]:
        pass

    def get_today_tasks(self) -> List["Task"]:
        pass

    def detect_conflicts(self) -> List["Task"]:
        pass

    def generate_recurring_tasks(self) -> List["Task"]:
        pass
