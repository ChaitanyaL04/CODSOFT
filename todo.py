
import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks to show.")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks):
            status = "✔️" if task['done'] else "❌"
            print(f"{idx + 1}. {task['task']} [{status}]")

# Add a task
def add_task(tasks):
    task_name = input("Enter task description: ")
    tasks.append({"task": task_name, "done": False})
    print("✅ Task added!")

# Mark a task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no]['done'] = True
            print("✅ Task marked as done!")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            removed = tasks.pop(task_no)
            print(f"🗑️ Deleted task: {removed['task']}")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n📋 TO-DO LIST MENU:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❗ Invalid option. Please choose between 1-5.")

if __name__ == "__main__":
    main()
