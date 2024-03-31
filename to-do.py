class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] += " - Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("Your tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("No tasks to display.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the task index to mark as complete: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            task_index = int(input("Enter the task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()
