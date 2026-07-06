import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_mark_complete_updates_status():
    task = Task(title="Walk the dog", category="Exercise", due_time="today")

    task.mark_complete()

    assert task.completed is True


def test_pet_add_task_increases_task_count():
    pet = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    task = Task(title="Feed dinner", category="Care", due_time="6:00 PM")

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1


def test_scheduler_generate_recurring_tasks_for_daily_recurrence():
    pet = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    task = Task(title="Walk the dog", category="Exercise", due_time="8:00 AM", due_date=date(2026, 7, 5), recurrence="daily")
    pet.add_task(task)

    owner = Owner(name="Alex", email="alex@example.com")
    owner.add_pet(pet)

    scheduler = Scheduler(owner=owner)
    recurring_tasks = scheduler.generate_recurring_tasks()

    assert len(recurring_tasks) == 1
    assert recurring_tasks[0].due_date == date(2026, 7, 6)
