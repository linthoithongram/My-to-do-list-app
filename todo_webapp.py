#import streamlit as st
#st.title("My To-Do List App")
#task = st.text_input("Enter a task: ")
import streamlit as st

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title("Simple To-Do List App")

menu = st.sidebar.radio("Menu", ["Add Tasks", "View Tasks", "Delete Task", "Exit"])

if menu == "Add Tasks":
    multi_task_input = st.text_input("Enter tasks (separated by commas):")
    if st.button("Add Tasks"):
        if multi_task_input.strip():
            # Split tasks by comma and strip spaces
            new_tasks = [task.strip() for task in multi_task_input.split(",") if task.strip()]
            st.session_state.tasks.extend(new_tasks)
            st.success(f"Added {len(new_tasks)} task(s).")
        else:
            st.warning("Please enter at least one task.")

elif menu == "View Tasks":
    if not st.session_state.tasks:
        st.info("There are no tasks in the list!")
    else:
        st.subheader("Your Tasks:")
        for i, task in enumerate(st.session_state.tasks):
            st.write(f"{i + 1}. {task}")

elif menu == "Delete Task":
    if not st.session_state.tasks:
        st.info("There are no tasks to delete!")
    else:
        st.subheader("Your Tasks:")
        for i, task in enumerate(st.session_state.tasks):
            st.write(f"{i + 1}. {task}")
        task_number = st.number_input("Enter the task number to delete:", min_value=1, max_value=len(st.session_state.tasks), step=1)
        if st.button("Delete"):
            removed = st.session_state.tasks.pop(task_number - 1)
            st.success(f"Removed: {removed}")

elif menu == "Exit":
    st.info("Goodbye! Have a great day.")
