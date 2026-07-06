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

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
