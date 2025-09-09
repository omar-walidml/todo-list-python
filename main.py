#main.py
import json
def load_tasks():
    #return a list of tasks initially empty
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]

def save_tasks(tasks):
    #save tasks to disk
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def display_menu():
    #print the menu options
    print("\n====To_Do List Menu====")
    print("1) Add task")
    print("2) View tasks")
    print("3) Mark task as done")
    print("4) Delete task")
    print("5) Exit")

def add_task(tasks):
    #ask user for description and append task to task list
    task = input("Enter your new task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f'Task "{task}" added successfully!')

def view_tasks(tasks):
    #print numbered tasks with status
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

def mark_done(tasks):
    #mark chosen tasks as done
    if not tasks:
        print("No tasks to mark as done.")
        return
    
    view_tasks(tasks)
    try:
        choice = int(input("Enter the number of the task to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print(f'Task "{tasks[choice - 1]["task"]}" marked as done!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
def delete_task(tasks):
    #delete a chosen task from the list
    if not tasks:
        print("No tasks to delete!")
        return
    view_tasks(tasks)
    try:
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f'Task"{removed["task"]}" deleted!')
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
            

if __name__ == "__main__":
    main()



    