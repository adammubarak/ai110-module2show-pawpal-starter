import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Demo Owner", "demo@example.com")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(owner=st.session_state.owner)

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+, your smart pet care scheduler!

This app helps you organize and prioritize care tasks for your pets.
"""
)

with st.expander("About PawPal+", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on time, priority, and scheduling constraints.

Features:
- Organize tasks by time
- Detect scheduling conflicts
- Support for recurring tasks
"""
    )

st.divider()

st.subheader("Manage Pets")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
if st.button("Add pet"):
    new_pet = Pet(name=pet_name, species=species, breed="", age=0)
    st.session_state.owner.add_pet(new_pet)
    st.session_state.scheduler = Scheduler(owner=st.session_state.owner)
    st.success(f"Added {pet_name}!")

if st.session_state.owner.get_pets():
    st.write("**Your pets:**")
    for pet in st.session_state.owner.get_pets():
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets added yet. Add one above!")

st.divider()

st.subheader("Add Tasks")
st.caption("Create tasks for your pets. They will be organized by time in the schedule.")

selected_pet = st.selectbox("Select pet", [pet.name for pet in st.session_state.owner.get_pets()] if st.session_state.owner.get_pets() else [])

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    due_time = st.text_input("Time (e.g., 8:00 AM)", value="8:00 AM")
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

task_category = st.selectbox("Category", ["Exercise", "Care", "Play", "Feeding", "Other"])

if st.button("Add task"):
    if selected_pet:
        pet_obj = next((p for p in st.session_state.owner.get_pets() if p.name == selected_pet), None)
        if pet_obj:
            new_task = Task(title=task_title, category=task_category, due_time=due_time, priority=priority)
            pet_obj.add_task(new_task)
            st.session_state.scheduler = Scheduler(owner=st.session_state.owner)
            st.success(f"Added '{task_title}' to {selected_pet}!")
    else:
        st.error("Please add a pet first.")

st.divider()

st.subheader("Schedule")
st.caption("Your tasks organized by time with conflict detection.")

if st.session_state.owner.get_all_tasks():
    sorted_tasks = st.session_state.scheduler.sort_by_time()
    
    task_data = []
    for task in sorted_tasks:
        task_data.append({
            "Time": task.due_time,
            "Title": task.title,
            "Category": task.category,
            "Priority": task.priority,
            "Status": "✓ Done" if task.completed else "⏳ Pending"
        })
    
    st.dataframe(task_data, use_container_width=True)
    
    conflicts = st.session_state.scheduler.detect_conflicts()
    if conflicts:
        st.warning("⚠️ Schedule Conflicts Detected:")
        for conflict in conflicts:
            st.write(f"- {conflict}")
    
else:
    st.info("No tasks yet. Add a pet and some tasks to see your schedule.")

st.divider()

st.subheader("Quick Actions")
if st.button("View all incomplete tasks"):
    incomplete_tasks = st.session_state.scheduler.filter_tasks(completed=False)
    if incomplete_tasks:
        st.write("**Incomplete tasks:**")
        for task in incomplete_tasks:
            st.write(f"- {task.title} at {task.due_time}")
    else:
        st.info("All tasks are done!")

if st.button("Show recurring tasks"):
    recurring = st.session_state.scheduler.generate_recurring_tasks()
    if recurring:
        st.write("**Upcoming recurring tasks:**")
        for task in recurring:
            st.write(f"- {task.title} on {task.due_date}")
    else:
        st.info("No recurring tasks found.")
