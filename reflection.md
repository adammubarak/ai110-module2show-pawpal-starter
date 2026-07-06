# PawPal+ Project Reflection

## 1. System Design

My initial UML design includes four main classes, Owner, Pet, Task, and Scheduler.
The Owner class represents the person using PawPal+. It is responsible for storing the owner's name, email, and list of pets. It can add pets, remove pets, and return the owner's pets.
The Pet class represents each animal in the system. It stores information such as the pet's name, species, breed, age, notes, and list of care tasks. It can add tasks and return the tasks connected to that pet.
The Task class represents one care responsibility, such as feeding, walking, medication, grooming, or a vet appointment. It stores the title, category, due time, priority, completion status, and recurrence information. It can be marked complete and checked to see if it is due today.
The Scheduler class handles the organization of tasks. It is responsible for sorting tasks, showing today's tasks, detecting conflicts, and later helping with recurring tasks.



**b. Design changes**
After reviewing the skeleton with AI feedback, I noticed that the relationship between Task, Pet, and Scheduler needed to be clearer. A Task may eventually need to know which Pet it belongs to so tasks do not become confusing when multiple pets are in the system.
I also noticed that having both Pet and Scheduler hold task lists could create duplicate task state. For now, I kept the design simple, but I plan to treat Pet as the place where tasks belong and Scheduler as the class that organizes or views those tasks.
I did not fully implement these changes yet because this phase is focused on the blueprint, but I documented them so I can refine the design during implementation.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

One tradeoff my scheduler makes is that conflict detection only checks for exact matching times. This keeps the algorithm simple and easy to understand, but it does not detect overlapping tasks with different start times and durations. For example, a 9:00 walk and a 9:15 grooming task might overlap, but my current method would not flag it unless the times are exactly the same.

I chose this simpler version because it is easier to test and fits the current scope of the project. A future version could compare start times and durations to catch more realistic scheduling conflicts.

## 3. AI Collaboration

**a. How you used AI**

I used my AI coding assistant to brainstorm the system design, create the UML diagram, generate the first class skeleton, and help implement the scheduler methods. The most useful features were being able to attach files, ask for focused feedback, and use agent/editing mode to update specific files like `pawpal_system.py`, `main.py`, and `app.py`.

Separate chat sessions helped me stay organized because each phase had a different goal. One chat focused on UML design, another focused on backend logic, another focused on algorithms, and another focused on testing. This made it easier to review AI suggestions without mixing unrelated tasks.

**b. Judgment and verification**

I did not accept every AI suggestion automatically. For example, when the scheduler design could have become more complex with overlapping time ranges and advanced calendar logic, I kept the conflict detection simple by checking exact matching times. This made the system easier to understand, test, and explain within the project scope.

I verified AI-generated code by running `python3 main.py`, `python3 -m py_compile pawpal_system.py`, and `python3 -m pytest`. I also tested the Streamlit app manually in the browser to confirm that adding a pet and scheduling tasks actually updated the app state.

## 4. Testing and Verification

**a. What you tested**

I tested the main behaviors that make PawPal+ work as a scheduling system. I tested that a task can be marked complete, that adding a task to a pet increases the pet's task list, and that tasks can be sorted in chronological order. I also tested filtering by completion status and pet name, recurring daily tasks, conflict detection when two tasks have the same time, and the edge case of a pet with no tasks.
These tests were important because they verify the core logic behind the app before relying on the Streamlit interface. If the backend classes do not work correctly, then the UI would only display incorrect or unreliable information. Testing the scheduler also helped confirm that the smarter features, like sorting, filtering, recurrence, and conflict warnings, behave as expected.


**b. Confidence**

I am fairly confident that the scheduler works correctly for the current project scope because the main behaviors are covered by automated pytest tests and the CLI demo runs successfully. I also manually tested the Streamlit app to confirm that pets and tasks can be added and displayed through the interface.
If I had more time, I would test more edge cases, such as overlapping tasks with different start times and durations, invalid time formats, empty task lists across multiple pets, duplicate pet names, and more recurrence patterns beyond daily and weekly tasks.



---

## 5. Reflection

**a. What went well**

The part that went well was separating the backend logic from the Streamlit interface. Building the classes first made it easier to test the system in the terminal before connecting it to the UI.

**b. What you would improve**

If I had another iteration, I would improve the scheduler so it detects overlapping tasks using both start times and durations instead of only checking exact matching times. I would also add more user controls in the Streamlit app for editing and deleting pets and tasks.

**c. Key takeaway**

The biggest thing I learned is that working with AI still requires human judgment. I had to act as the lead architect by deciding which suggestions fit the project, checking that the code matched the assignment, and verifying the system with tests and demos.
