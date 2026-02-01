from datetime import datetime
import sys
import json

def delete_entry(num) :
    remove_success = False
    try:
        with open("tasks.json", 'r') as file:
            task_contents = json.loads(file.read())
            task_count = 0
            new_task_contents = {}
            new_task_contents = []
        for task in task_contents:
            task_count += 1
            if task_count != num:
                new_task_contents.append({"date": task["date"], "description": task["description"]})
            else:
                print("Task", task_count, "removed from list")
                remove_success = True 
    except (FileNotFoundError, json.JSONDecodeError) :
        input("There was an error loading the file. Press Enter to continue...")
    if not remove_success:
        print("No task numbered", num)
        input("Press Enter to continue...")
        main_menu()

    try:
        with open("tasks.json", "w") as file:
            json.dump(new_task_contents, file, indent=4)
            input("Data saved successfully. Press Enter to continue")
    except Exception as e:
        print(f"Data not saved. An unexpected error occurred: {e}")
        input("Press Enter to continue")
    
    main_menu()

def new_entry():
    timestamp = datetime.now()
    entry_data = {}
    entry_data["date"] = str(timestamp)
    entry_data["description"] = input("Enter description for new task:")

    try:
        with open("tasks.json", "r") as file:
            entries = json.loads(file.read())
    except (FileNotFoundError, json.JSONDecodeError):
        entries = []

    entries.append(entry_data)

    try:
        with open("tasks.json", "w") as file:
            json.dump(entries, file, indent=4)
    except Exception as e:
        print(f"Data not saved. An unexpected error occurred: {e}")
        input("Press Enter to continue")

    main_menu()

# quit the application
def quit_application():
    print("\033c", end="")
    print("Thank you for using the task manager app. Goodbye!")
    sys.exit(0)

def list_current_tasks() :
    task_number = 0
    try:
        with open("tasks.json", 'r') as file:
            task_contents = json.loads(file.read())
            for task in task_contents:
                task_number += 1
                print(task_number, "-", task["description"])
    except FileNotFoundError:
        print("There are no tasks - file does not exist")
    except json.JSONDecodeError:
        print("There are no tasks - file format error")

def main_menu():
    print("\033c", end="")
    print("Task List Manager\n")
    list_current_tasks()

    command = input("\nEnter to N to add a new task, a task number to remove a task, or Q to quit: ")

    if command == 'N' or command == 'n' :
        new_entry()
    elif command == 'Q' or command == 'q' :
        quit_application()
    else :
        try:
            entry_number = int(command)
            if entry_number > 0:
                delete_entry(entry_number)
            else:
                input("Please enter a valid entry number. Press Enter to try again.")
                main_menu()
        except(ValueError):
            print("This was an invalid command. Press Enter to try again")
            main_menu()

main_menu()
