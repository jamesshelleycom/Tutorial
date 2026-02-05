from datetime import datetime
import sys
import json

filename = "OOP_library.json"

class Book:

    def __init__(self, title, author, available) :
        self.title = title
        self.author = author
        self.available = available
        
    def checkout_book(self):
        self.available = False

    def return_book(self):
        self.available = True

    def display_book(self, num) :
        location = ""
        if self.available :
            location = "In Library"
        else:
            location = "On Loan"
        print(f"{num} - {self.title} ({self.author}) - {location}") 

    def to_dict(self):
        return {"title": self.title, "author": self.author, "available": self.available}
                  
def add_book(title, author, available) :
    library_contents = load_library()
    if not library_contents :
        library_contents = []
    
    new_book_data = {"title": title, "author": author, "available": available}
    library_contents.append(new_book_data)
    if save_library(library_contents) :
        return True
    else :
        return False


def save_library(library_contents) :
    try:
        with open(filename, "w") as file:
            json.dump(library_contents, file, indent=4)
            return True
    except Exception as e:
        return False

def collect_metadata() :
    new_book = {}
    new_book["title"] = input("Enter book title: ")
    new_book["author"] = input("Enter book author: ")
    new_book["available"] = True
    return new_book

def new_book() :
    new_book = collect_metadata()
    if add_book(new_book["title"], new_book["author"], new_book["available"]) :
        print(new_book["title"], "was successfully added")
    else :
        print("Book was not added to library")
    input("Press enter to continue...")
    main_menu()

def load_library() :
    try:
        with open(filename, 'r') as file:
            file_contents = json.loads(file.read())
            return file_contents
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# quit the application
def quit_application():
    print("\033c", end="")
    print("Thank you for using the Library Catalogue App!")
    sys.exit(0)

def switch_book_status(num) :
    catalogue = load_library()
    if num > len(catalogue):
        input("Book not found. Press enter to continue...")
        main_menu()
        return
    index = 0
    for book in catalogue :
        index += 1
        if index == num : ## we found the book
            change_book = Book(book['title'], book['author'], book['available'])
            if change_book.available :
                change_book.checkout_book()
            else :
                change_book.return_book()
    index = 0
    new_catalogue = []
    for book in catalogue :
        index += 1
        if index == num :
            new_catalogue.append(change_book.to_dict())
        else :
            new_catalogue.append(book)
    save_library(new_catalogue)
    main_menu()

def main_menu():
    print("\033c", end="")
    print("Library Catalogue\n")
    display_library()
    command = input("\nEnter to N to add a new book, a book number to check in/out, or Q to quit: ")

    if command == 'N' or command == 'n' :
        new_book()
    elif command == 'Q' or command == 'q' :
        quit_application()
    else :
        try:
            entry_number = int(command)
            if entry_number > 0:
                switch_book_status(entry_number)
            else:
                input("Please enter a valid entry number. Press Enter to try again.")
                main_menu()
        except(ValueError):
            print("This was an invalid command. Press Enter to try again")
            main_menu()

    
def display_library():
    catalogue = load_library()
    num = 0
    if catalogue :
        for book in catalogue :
            num += 1
            catalogue_item = Book(book['title'], book['author'], book['available'])
            catalogue_item.display_book(num)
    else :
        print("Library is empty")


main_menu()
