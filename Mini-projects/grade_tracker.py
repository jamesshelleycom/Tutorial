from datetime import datetime
import sys
import json

def new_entry():
    timestamp = datetime.now()
    input_fields = ["student_number", "math_grade", "english_grade", "science_grade"]
    entry_data = {}
    print("\033c", end="")
    print("Enter student information and marks as of", timestamp.strftime("%A, %B %d, %Y"), "\n")
    for n in input_fields:
        while True:
            try:
                prompt = "Enter value for " + n + " > "
                user_input = int(input(prompt))
                entry_data[n] = user_input
                break
            except ValueError:
                print("You must enter a valid integer")
    try:
        with open("grades.json", "r") as file:
            entries = json.loads(file.read())
    except (FileNotFoundError, json.JSONDecodeError):
        entries = []
    
    entries.append(entry_data)
    
    try:
        with open("grades.json", "w") as file:
            json.dump(entries, file, indent=4)
            input("Data saved successfully. Press Enter to continue")
    except Exception as e:
        print(f"Data not saved. An unexpected error occurred: {e}")
        input("Press Enter to continue")
    
    main_menu()

# quit the application
def quit_application():
    print("\033c", end="")
    print("Thank you for using this app. Goodbye!")
    sys.exit(0)

def read_entry(num) :
    try:
        with open("grades.json", 'r') as file:
            grade_contents = json.loads(file.read())
            for student_entry in grade_contents:
                if student_entry["student_number"] == num : ## We found the student
                    print("Details for student #", num)
                    subjects = 0
                    total_sum = 0
                    for key, value in student_entry.items(): ## compile the fields
                        if "_grade" in key :
                            subjects += 1
                            total_sum += value
                            print(key, "=", value)
                    if subjects > 0 :
                        final_grade = total_sum / subjects
                        print("Grade average is ", final_grade)
                    else:
                        print("Grade average is", total_sum)
            input("Press Enter to continue...")
    except FileNotFoundError:
        input("Error: There is no file! Press Enter to continue...")
    if not subjects:
        print("No grades found for student #", num)
        input("Press Enter to continue...")
    main_menu()

def main_menu():
    print("\033c", end="")
    print("Student Grade Tracker\n")

    command = input("Enter to N to add a new student, a student number to view a grade, or Q to quit: ")

    if command == 'N' or command == 'n' :
        new_entry()
    elif command == 'Q' or command == 'q' :
        quit_application()
    else :
        try:
            entry_number = int(command)
            if entry_number > 0:
                read_entry(entry_number)
            else:
                input("Please enter a valid entry number. Press Enter to try again.")
                main_menu()
        except(ValueError):
            print("This was an invalid command. Press Enter to try again")
            main_menu()

main_menu()
