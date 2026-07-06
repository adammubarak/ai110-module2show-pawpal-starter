# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

## Features

**Pet Management**
- Add multiple pets with name, species, and details
- Keep track of all your pets in one place

**Task Organization**
- Create care tasks with title, time, category, and priority level
- Assign tasks to specific pets
- Mark tasks as complete

**Smart Scheduling**
- Automatically sort tasks in chronological order
- Filter tasks by completion status (show pending or completed)
- View tasks for a specific pet
- See all tasks in a clear table format with time, priority, and status

**Conflict Detection**
- Automatically detect and warn when two tasks are scheduled at the same time
- Receive clear warnings to help you reschedule overlapping tasks

**Recurring Tasks**
- Set up daily recurring tasks that automatically generate for the next day
- Set up weekly recurring tasks that automatically generate for the next week
- View upcoming recurring task instances

**User Interfaces**
- **Streamlit Web App** (app.py): Interactive web-based interface to manage pets and tasks
- **CLI Demo** (main.py): Command-line interface demonstrating all scheduling features

**Backend**
- Clean, beginner-friendly Python dataclasses (Owner, Pet, Task, Scheduler)
- Full test coverage with pytest


## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

## 🖥️ Sample Output

```text
Today's Schedule
----------------
- Morning walk (today) - Priority: high
- Clean litter box (today) - Priority: high
```
## Smarter Scheduling

PawPal+ now includes basic scheduling algorithms that make the system more useful for pet care planning.

- Sorting behavior: `Scheduler.sort_by_time()` sorts tasks by their scheduled time so the daily plan appears in order.
- Filtering behavior: `Scheduler.filter_tasks()` can filter tasks by pet name or completion status, such as showing only incomplete tasks.
- Recurring task logic: `Scheduler.generate_recurring_tasks()` creates the next daily or weekly task after a recurring task is completed.
- Conflict detection: `Scheduler.detect_conflicts()` checks for tasks scheduled at the exact same time and returns a warning instead of crashing the program.
## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:
platform darwin -- Python 3.13.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/mubarak/ai110-module3tinker-themoodmachine-starter/ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collected 8 items                                                                         

tests/test_pawpal.py ........                                                       [100%]
Confidence Level: ⭐⭐⭐⭐☆ (4/5)

I am fairly confident in the system because the automated tests cover the main scheduler behaviors, including sorting, filtering, recurrence, conflict detection, task completion, and empty pet task lists. I would increase confidence by testing more complex overlapping schedules and additional recurrence patterns.

```
## Testing PawPal+

Run the automated tests with:

```bash
python3 -m pytest
```

The test suite verifies the main PawPal+ system behaviors, including task completion, adding tasks to pets, sorting tasks in chronological order, filtering by completion status and pet name, recurring daily tasks, conflict detection for duplicate times, and the empty-pet edge case.

Successful test output:

```text
PASTE YOUR PYTEST OUTPUT HERE
```

Confidence Level: ⭐⭐⭐⭐☆ (4/5)

I am fairly confident in the system because the main scheduler behaviors are covered by automated tests. I would increase confidence further by testing more complex overlapping task durations and more recurrence patterns.
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

The PawPal+ app lets a pet owner manage pets, add care tasks, and view a smart schedule. The Streamlit UI connects directly to the backend classes in `pawpal_system.py`.

1. The user opens the Streamlit app with `streamlit run app.py`.
2. The user adds a pet by entering the pet name and selecting a species.
3. The user creates care tasks with a title, time, category, and priority.
4. The schedule table displays tasks in chronological order using the Scheduler sorting logic.
5. If two tasks are scheduled at the same time, the app displays a conflict warning so the owner knows to adjust the schedule.
6. The user can view incomplete tasks and use the CLI demo in `main.py` to verify backend scheduling behavior.

Example CLI output from `python3 main.py`:

```text
Today's Schedule
----------------
- Morning walk (today) - Priority: high
- Clean litter box (today) - Priority: high
```
