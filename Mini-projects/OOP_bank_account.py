import sys
import json
import random

class BankAccount(object):

    def __init__(self, name, accountType, balance = 0):
        self.name = name
        self.accountType = accountType
        self.accountNumber = random.randint(10000, 999999)
        self.balance = balance
        self.filename=str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"

    def account_balance(self) :
        return self.balance
    
    def deposit(self, amount) :
        self.balance += amount
        return
    
    def withdraw(self, amount) :
        if amount <= self.balance :
            self.balance -= amount
            return True
        else :
            return False
    
    def showAccountNumber(self) :
        return self.accountNumber
    
    def showName(self) :
        return self.name
    
    def showType(self) :
        return self.accountType
    
    def showTransactions(self) :
        try:
            with open(self.filename, "r") as file:
                transaction_list = file.read()
            return transaction_list
        except Exception as e:
            return ""
        
    def saveTransactions(self, data) :
        try:
            with open(self.filename, "w") as file:
                file.write(data)
        except Exception as e:
            return False
    
    def recordTransaction(self, amount, transaction_type):
        transactions_file = self.showTransactions()
        transaction_details = f"\n{transaction_type} of ${amount:.2f}"
        transactions_file += transaction_details
        self.saveTransactions(transactions_file)    

def make_deposit():
    amount = float(input("Enter amount to deposit > $"))
    user_account.deposit(amount)
    user_account.recordTransaction(amount, "deposit")
    main_menu()

def make_withdrawal():
    amount = float(input("Enter amount to withdraw > $"))
    if user_account.withdraw(amount) :
        user_account.recordTransaction(amount, "withdraw")
        input("Withdraw success. Press enter to continue...")
    else :
        input("You cannot withdraw that much! Press enter to continue...")
    main_menu()

# quit the application
def quit_application():
    print("\033c", end="")
    transactions = user_account.showTransactions()
    if transactions != "" :
        print("Here are your transactions today:")
        print(transactions)
    print("\nThank you for visiting the bank today!")
    sys.exit(0)

def main_menu():
    print("\033c", end="")
    print(f"Hello, {user_account.showName()}!\n\nYour current balance is ${user_account.account_balance():.2f}\nYour account type is {user_account.showType()}\nYour account number is #{user_account.showAccountNumber()}\n")    
    command = input("Please press D to deposit, W to withdraw, or Q to quit > ")

    if command == 'D' or command == 'd' :
        make_deposit()
    elif command == 'Q' or command == 'q' :
        quit_application()
    elif command == "W" or command == "w" :
        make_withdrawal()
    else :
        input("Please enter a valid entry. Press Enter to try again.")
        main_menu()

## Start the program 
print("\033c", end="")
print("Welcome to the bank!\n\nTo begin, please create an account\n")
name = input("Enter your name > ")
type_int = int(input("Press 1 to open a checking account, press 2 to open a savings account > "))
type_string = ""
if type_int == 1 :
    type_string = "checking"
elif type_int == 2 :
    type_string = "savings"
else :
    print("Come back when you are ready to pick an account")
    quit_application()
user_account = BankAccount(name, type_string)
main_menu()
