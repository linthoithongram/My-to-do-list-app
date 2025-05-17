#import streamlit as st
#st.title("My To-Do List App")
#task = st.text_input("Enter a task: ")
import streamlit as st
import json
import os
from datetime import datetime, timedelta

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        print("Loading tasks from file...")
        with open(TASK_FILE, "r") as f:
            data = json.load(f)
        now = datetime.now()
        data = [item for item in data if now - datetime.fromisoformat(item["time"]) < timedelta(hours=24)]
        print("Loaded tasks:", data)
        return data
    print("No existing task file found.")
    return []

def save_tasks(task_list):
    print("Saving tasks to file:", task_list)
    with open(TASK_FILE, "w") as f:
        json.dump(task_list, f)

st.title("📝 My To-Do List (24-Hour Tasks)")

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

new_tasks_input = st.text_input("Enter tasks separated by commas:")

if st.button("Add Tasks"):
    new_tasks = [t.strip() for t in new_tasks_input.split(",") if t.strip()]
    for task in new_tasks:
        st.session_state.tasks.append({"task": task, "time": datetime.now().isoformat()})
    save_tasks(st.session_state.tasks)
    st.success(f"Added: {', '.join([t['task'] for t in st.session_state.tasks[-len(new_tasks):]])}")

st.subheader("Your Tasks (stay for 24 hours):")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            st.write(f"{i+1}. {task['task']}")
        with col2:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                save_tasks(st.session_state.tasks)
                st.experimental_rerun()
else:
    st.info("No tasks yet. Add some above!")

