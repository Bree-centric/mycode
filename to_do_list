class Task:
    def __init__(self, title, description, priority='Low', completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed

    def __str__(self):
        return f"{self.title} - Priority: {self.priority}, Completed: {'Yes' if self.completed else 'No'}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        self.tasks[index].completed = True

    def delete_task(self, index):
        del self.tasks[index]

def main():
    todo_list = ToDoList()

    while True:
        print("\nTODO LIST MENU:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (Low/Medium/High): ")
            task = Task(title, description, priority)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            if todo_list.tasks:
                print("\nTASKS:")
                todo_list.view_tasks()
            else:
                print("No tasks found.")

        elif choice == '3':
            index = int(input("Enter the index of the task you want to complete: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                todo_list.complete_task(index)
                print("Task marked as completed.")
            else:
                print("Invalid index.")

        elif choice == '4':
            index = int(input("Enter the index of the task you want to delete: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                todo_list.delete_task(index)
                print("Task deleted successfully.")
            else:
                print("Invalid index.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

