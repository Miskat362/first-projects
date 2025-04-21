import os

TASKS_FILE = "tasks.txt"

def add_task(task):
    with open(TASKS_FILE, "a") as file:
        file.write(task + "\n")
    print(f"Added: {task}")

def view_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        if tasks:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
        else:
            print("\nNo tasks yet!")
    else:
        print("\nNo tasks yet!")

def delete_task(task_number):
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open(TASKS_FILE, "w") as file:
                file.writelines(tasks)
            print(f"Deleted: {removed_task.strip()}")
        else:
            print("Invalid task number!")
    else:
        print("\nNo tasks to delete!")

def main():
    while True:
        print("\nOptions: add / view / delete / exit")
        choice = input("Enter command: ").strip().lower()
        
        if choice == "add":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "view":
            view_tasks()
        elif choice == "delete":
            view_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()