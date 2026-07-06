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


def test_scheduler_sort_by_time_returns_chronological_order():
    owner = Owner(name="Alex", email="alex@example.com")
    pet = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    owner.add_pet(pet)

    pet.add_task(Task(title="Dinner", category="Care", due_time="6:00 PM"))
    pet.add_task(Task(title="Morning walk", category="Exercise", due_time="8:00 AM"))
    pet.add_task(Task(title="Afternoon play", category="Play", due_time="3:00 PM"))

    scheduler = Scheduler(owner=owner)
    ordered_tasks = scheduler.sort_by_time()

    assert [task.title for task in ordered_tasks] == ["Morning walk", "Afternoon play", "Dinner"]


def test_scheduler_filter_tasks_returns_only_incomplete_tasks():
    owner = Owner(name="Alex", email="alex@example.com")
    pet = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    owner.add_pet(pet)

    incomplete_task = Task(title="Feed dinner", category="Care", due_time="6:00 PM")
    complete_task = Task(title="Walk", category="Exercise", due_time="8:00 AM")
    complete_task.mark_complete()

    pet.add_task(incomplete_task)
    pet.add_task(complete_task)

    scheduler = Scheduler(owner=owner)
    filtered_tasks = scheduler.filter_tasks(completed=False)

    assert len(filtered_tasks) == 1
    assert filtered_tasks[0].title == "Feed dinner"


def test_scheduler_filter_tasks_by_pet_name_returns_only_that_pets_tasks():
    owner = Owner(name="Alex", email="alex@example.com")
    luna = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    max_pet = Pet(name="Max", species="Cat", breed="Siamese", age=2)
    owner.add_pet(luna)
    owner.add_pet(max_pet)

    luna.add_task(Task(title="Walk", category="Exercise", due_time="8:00 AM"))
    max_pet.add_task(Task(title="Clean litter box", category="Care", due_time="7:00 AM"))

    scheduler = Scheduler(owner=owner)
    filtered_tasks = scheduler.filter_tasks(pet_name="Luna")

    assert len(filtered_tasks) == 1
    assert filtered_tasks[0].title == "Walk"


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


def test_scheduler_detect_conflicts_flags_duplicate_due_times():
    owner = Owner(name="Alex", email="alex@example.com")
    pet = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    owner.add_pet(pet)

    pet.add_task(Task(title="Morning walk", category="Exercise", due_time="8:00 AM"))
    pet.add_task(Task(title="Feed breakfast", category="Care", due_time="8:00 AM"))

    scheduler = Scheduler(owner=owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "Conflict:" in conflicts[0]


def test_pet_with_no_tasks_returns_empty_list():
    pet = Pet(name="Luna", species="Dog", breed="Labrador", age=3)

    assert pet.get_tasks() == []
