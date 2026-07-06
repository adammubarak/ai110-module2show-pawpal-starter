from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner(name="Alex", email="alex@example.com")

    luna = Pet(name="Luna", species="Dog", breed="Labrador", age=3)
    max_pet = Pet(name="Max", species="Cat", breed="Siamese", age=2)

    owner.add_pet(luna)
    owner.add_pet(max_pet)

    luna.add_task(Task(title="Morning walk", category="Exercise", due_time="today", priority="high"))
    luna.add_task(Task(title="Feed dinner", category="Care", due_time="6:00 PM", priority="medium"))
    max_pet.add_task(Task(title="Clean litter box", category="Care", due_time="today", priority="high"))

    scheduler = Scheduler(owner=owner)

    print("Today's Schedule")
    print("----------------")
    for task in scheduler.get_today_tasks():
        print(f"- {task.title} ({task.due_time}) - Priority: {task.priority}")


if __name__ == "__main__":
    main()
