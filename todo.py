import json

class Task:
    def _init_(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        # Save tasks as a list of dictionaries
        json.dump([task._dict_ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks_data = json.load(f)
            print(tasks_data)  # Debugging: print the loaded tasks
            return [Task(task['title'], task['description'], task['category']) for task in tasks_data]
    except FileNotFoundError:
        return []

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task.completed else "Not completed"
        print(f"{i}. {task.title} - {task.description} ({task.category}) [{status}]")

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category: ")

    # Debugging: print the task data before appending
    print(f"Title: {title}, Description: {description}, Category: {category}")

    # Check if any of the fields are empty
    if not title or not description or not category:
        print("Error: All fields (title, description, category) must be filled.")
        return

    tasks.append(Task(title, description, category))

def mark_task_completed(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number].mark_completed()
    else:
        print("Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
    else:
        print("Invalid task number.")

# Main Program Execution
tasks = load_tasks()

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")
    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        display_tasks(tasks)
    elif choice == '3':
        mark_task_completed(tasks)
    elif choice == '4':
        delete_task(tasks)
    elif choice == '5':
        save_tasks(tasks)
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
