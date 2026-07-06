import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pawpal_system import Pet, Task


def test_task_mark_complete_updates_status():
    task = Task(title="Walk the dog", category="Exercise", due_time="today")

    task.mark_complete()

    assert task.completed is True


def test_pet_add_task_increases_task_count():
    pet = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    task = Task(title="Feed dinner", category="Care", due_time="6:00 PM")

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1
