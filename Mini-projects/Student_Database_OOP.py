from datetime import datetime
import sys
import json

filename = "OOP_students.json"

available_courses = ["English", "Math", "Science"]

class Student:

    def __init__(self, name, num, age, courses) :
        self.name = name
        self.num = num
        self.age = age
        self.courses = courses
        
    def save_student(self) :
        try:
            with open(filename, "r") as file:
                entries = json.loads(file.read())
        except (FileNotFoundError, json.JSONDecodeError):
            entries = []
        
        entry_data = {"name": self.name, "num": self.num, "age": self.age, "courses": self.courses}

        entries.append(entry_data)
        
        try:
            with open(filename, "w") as file:
                json.dump(entries, file, indent=4)
                return True
        except Exception as e:
            return False
        
    def calculate_average(self):
        if not self.courses:
            return 0
        total = sum(course["grade"] for course in self.courses)
        return total / len(self.courses)

    def display_info(self):
        print(f"Details for {self.name} (Student #{self.num})\n")
        for course in self.courses:
            print(course["name"], "=", course["grade"])
        print("Grade average is", self.calculate_average())
        
def add_student() :
    new_student = {}
    new_student["name"] = input("Enter student name:")
    new_student["num"] = int(input("Enter student number:"))
    new_student["age"] = int(input("Enter student age:"))
    new_student["courses"] = []
    for n in available_courses :
        new_course = {}
        new_course["name"] = n
        prompt = "Enter grade for the " + n + " course:"
        new_course["grade"] = int(input(prompt))
        new_student["courses"].append(new_course)
    return new_student

def load_student(num) :
    try:
        with open(filename, 'r') as file:
            file_contents = json.loads(file.read())
            for student_entry in file_contents:
                if student_entry["num"] == num : ## We found the student
                    return student_entry
    except FileNotFoundError:
        input("Error: There is no file! Press Enter to continue...")
        return None
    return None

def view_student(num) :
    student_data = load_student(num)

    if student_data :
        student = Student(student_data["name"], student_data["num"], student_data["age"], student_data["courses"])
        student.display_info()
        input("Press enter to continue...")
        main_menu()
    else :
        input("Student not found. Press enter to continue...")
        main_menu()

def add_student_menu() :

    new_student = add_student()
    student_to_add = Student(new_student["name"], new_student["num"], new_student["age"], new_student["courses"])
    student_to_add.save_student()
    main_menu()





# quit the application
def quit_application():
    print("\033c", end="")
    print("Thank you for using the Student Database App!")
    sys.exit(0)

def main_menu():
    print("\033c", end="")
    print("Student Database App\n")

    command = input("Enter to N to add a new student, a student number to view a grade, or Q to quit: ")

    if command == 'N' or command == 'n' :
        add_student_menu()
    elif command == 'Q' or command == 'q' :
        quit_application()
    else :
        try:
            entry_number = int(command)
            if entry_number > 0:
                view_student(entry_number)
            else:
                input("Please enter a valid entry number. Press Enter to try again.")
                main_menu()
        except(ValueError):
            print("This was an invalid command. Press Enter to try again")
            main_menu()

main_menu()
