class Task:
    def __init__(self, name, status="Pending", description=""):
        self.name = name
        self.status = status
        self.description = description


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description=""):
        task = Task(name, description=description)
        self.tasks.append(task)
        print(f'Task "{name}" added to the to-do list.')

    def list_tasks(self):
        if not self.tasks:
            print("The to-do list is empty.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(f"- {task.name}")

    def mark_task_completed(self, name):
        for task in self.tasks:
            if task.name == name:
                task.status = "Completed"
                print(f'Task "{name}" marked as completed.')
                return
        print(f'Task "{name}" not found in the to-do list.')

    def clear_all_tasks(self):
        self.tasks = []
        print("All tasks cleared from the to-do list.")


def main():
    todo_manager = ToDoListManager()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter the task name: ")
            description = input("Enter the task description (optional): ")
            todo_manager.add_task(name, description)
        elif choice == "2":
            todo_manager.list_tasks()
        elif choice == "3":
            name = input("Enter the task name to mark as completed: ")
            todo_manager.mark_task_completed(name)
        elif choice == "4":
            todo_manager.clear_all_tasks()
        elif choice == "5":
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
