from datetime import datetime
import sys
import json

def diary_content() :
    file_name = "diary_content.json"
    try:
        with open(file_name) as diary_file :
            past_entries = json.loads(diary_file.read())
            diary_file.close()
            return len(past_entries)
    except(FileNotFoundError) :
        return 0

def new_entry():
    timestamp = datetime.now()
    print("\033c", end="")
    print("Enter a diary entry for today,", timestamp.strftime("%A, %B %d, %Y"), "\n")
    entry_data = input("> ")
    entry_dict = {"date": str(timestamp), "display_date": timestamp.strftime("%A, %B %d, %Y"), "entry": entry_data}    
    try:
        with open("diary_content.json", "r") as file:
            entries = json.loads(file.read())
    except FileNotFoundError:
        entries = []
    # Add the new entry
    entries.append(entry_dict)
    # Write the whole list back
    with open("diary_content.json", "w") as file:
        file.write(json.dumps(entries))
    main_menu()

def quit_application():
    print("\033c", end="")
    print("Thank you for using this app. Goodbye!")
    sys.exit(0)

def read_entry(num) :
    num -= 1
    try:
        with open("diary_content.json", 'r') as file:
            diary_contents = json.loads(file.read())
            file.close()
            entry = diary_contents[num]
            print("\033c", end="")
            print(f"On {entry["display_date"]} you wrote:\n\n{entry["entry"]}\n")
            input("Press Enter to continue...")
    except FileNotFoundError:
        input("Error: There is no file! Press Enter to continue...")
    main_menu()

def main_menu():
    diary_status = diary_content()

    print("\033c", end="")
    print("Welcome to the Diary Application\n")

    if diary_status > 0 :
        print(f"You have {diary_status} entries in your diary\n")
    else:          
        print("You have not started a diary yet\n")

    command = input("Enter to N to add a new entry, an entry number to view a past entry, or Q to quit: ")

    if command == 'N' or command == 'n' :
        new_entry()
    elif command == 'Q' or command == 'q' :
        quit_application()
    else :
        try:
            entry_number = int(command)
            if entry_number != 0 and entry_number <= diary_status:
                read_entry(entry_number)
            else:
                input("Please enter a valid entry number. Press Enter to try again.")
                main_menu()
        except(ValueError):
            print("This was an invalid command. Press Enter to try again")
            main_menu()

main_menu()
