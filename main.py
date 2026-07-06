from datetime import date

from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner(name="Alex", email="alex@example.com")

    luna = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    max_pet = Pet(name="Max", species="Cat", breed="Siamese", age=2)

    owner.add_pet(luna)
    owner.add_pet(max_pet)

    morning_walk = Task(
        title="Morning walk",
        category="Exercise",
        due_time="8:00 AM",
        priority="high",
        due_date=date.today(),
        recurrence="daily",
    )
    feed_dinner = Task(title="Feed dinner", category="Care", due_time="6:00 PM", priority="medium")
    litter_box = Task(title="Clean litter box", category="Care", due_time="7:00 AM", priority="high")
    extra_walk = Task(title="Evening walk", category="Exercise", due_time="8:00 AM", priority="medium")

    luna.add_task(morning_walk)
    luna.add_task(feed_dinner)
    max_pet.add_task(litter_box)
    luna.add_task(extra_walk)

    scheduler = Scheduler(owner=owner)

    print("Unsorted Tasks")
    print("--------------")
    for task in scheduler._get_tasks():
        print(f"- {task.title} ({task.due_time})")

    print("\nSorted Tasks")
    print("------------")
    for task in scheduler.sort_by_time():
        print(f"- {task.title} ({task.due_time})")

    print("\nIncomplete Tasks")
    print("----------------")
    for task in scheduler.filter_tasks(completed=False):
        print(f"- {task.title} ({task.due_time})")

    print("\nLuna's Tasks")
    print("------------")
    for task in scheduler.filter_tasks(pet_name="Luna"):
        print(f"- {task.title} ({task.due_time})")

    print("\nRecurring Task Copies")
    print("---------------------")
    for task in scheduler.generate_recurring_tasks():
        print(f"- {task.title} ({task.due_date})")

    print("\nConflict Warnings")
    print("-----------------")
    for warning in scheduler.detect_conflicts():
        print(f"- {warning}")


if __name__ == "__main__":
    main()
