class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def Is_Done(self):
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f'Task "{title}" added.')

    def mark_task_completed(self):
        if not self.tasks:
            print('No tasks to mark as completed.')
        else:
            self.tasks[-1].Is_Done()
            print(f'Task "{self.tasks[-1].title}" marked as completed.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for task in self.tasks:
                status = "Completed" if task.completed else "Not Completed"
                print(f'- {task.title} ({status})')

    def exit_task_manager(self):
        print('Exiting the Task Manager. Goodbye!')
        exit()

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)

        elif choice == '2':
            task_manager.mark_task_completed()

        elif choice == '3':
            task_manager.display_tasks()

        elif choice == '4':
            task_manager.exit_task_manager()

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
