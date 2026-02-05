import sys
import json

filename = "OOP_inventory.json"

class Product:

    def __init__(self, name, price, quantity) :
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def remove_product(self, num):
        if self.quantity >= num :
            self.quantity -= num
            return num
        else :
            return False
    
    def add_product(self, num):
        self.quantity += num
    
    def display_inventory_stock(self) :
        quantity = ""
        if self.quantity :
            quantity = quantity = f"{self.quantity} in stock"
        else:
            quantity = "Out of stock"
        return f"{self.name} (${self.price:.2f}) - {quantity}" 

    def to_dict(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

## Functions outside of class Product

def add_product(name, price, quantity) :
    inventory_contents = load_inventory()
    if not inventory_contents :
        inventory_contents = []
    
    new_product_data = {"name": name, "price": price, "quantity": quantity}
    inventory_contents.append(new_product_data)
    if save_inventory_database(inventory_contents) :
        return True
    else :
        return False


def save_inventory_database(inventory_contents) :
    try:
        with open(filename, "w") as file:
            json.dump(inventory_contents, file, indent=4)
            return True
    except Exception as e:
        return False

def collect_product_data() :
    new_product = {}
    new_product["name"] = input("New product name: ")
    new_product["price"] = float(input("New product price: $"))
    new_product["quantity"] = int(input("New product inventory: "))
    return new_product

def new_product() :
    new_product = collect_product_data()
    if add_product(new_product["name"], new_product["price"], new_product["quantity"]) :
        print(new_product["quantity"], "new", new_product["name"], "were successfully added to the inventory")
    else :
        print("New product was not added to inventory")
    input("Press enter to continue...")
    main_menu()

def load_inventory() :
    try:
        with open(filename, 'r') as file:
            file_contents = json.loads(file.read())
            return file_contents
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# quit the application
def quit_application():
    print("\033c", end="")
    print("Thank you for using this inventory app!")
    sys.exit(0)

def restock_item(num) :
    inventory = load_inventory()
    if num > len(inventory):
        input("Product not found. Press enter to continue...")
        main_menu()
        return
    index = 0
    for product in inventory :
        index += 1
        if index == num : ## we found the item!
            restock_item = Product(product['name'], product['price'], product['quantity'])
            prompt = "Enter the number of " + restock_item.name + " you are adding to the inventory > "
            restock_item.quantity += int(input(prompt))

    index = 0
    new_inventory = []
    for product in inventory :
        index += 1
        if index == num :
            new_inventory.append(restock_item.to_dict())
        else :
            new_inventory.append(product)
    save_inventory_database(new_inventory)
    main_menu()

def sell_item(num) :
    inventory = load_inventory()
    if num > len(inventory):
        input("Product not found. Press enter to continue...")
        main_menu()
        return
    index = 0
    for product in inventory :
        index += 1
        if index == num : ## we found the item!
            restock_item = Product(product['name'], product['price'], product['quantity'])
            prompt = "Enter the number of " + restock_item.name + " you are selling from the inventory > "
            quantity_sold = int(input(prompt))
            if quantity_sold > restock_item.quantity :
                input("We don't have enough inventory for that! Press enter to continue...")
                main_menu()
            else :
                restock_item.remove_product(quantity_sold)
                input("Transaction complete. Press enter to continue...")

    index = 0
    new_inventory = []
    for product in inventory :
        index += 1
        if index == num :
            new_inventory.append(restock_item.to_dict())
        else :
            new_inventory.append(product)
    save_inventory_database(new_inventory)
    main_menu()


def main_menu():
    print("\033c", end="")
    print("Welcome to the Storefront!\n")
    display_inventory()
    command = input("\nEnter to N to add a new product, R to restock inventory, an index number to sell a product, or Q to quit: ")

    if command == 'N' or command == 'n' :
        new_product()
    elif command == 'Q' or command == 'q' :
        quit_application()
    elif command == "R" or command == "r" :
        menu_item = int(input("Which item number would you like to restock?"))
        restock_item(menu_item)
    else :
        try:
            entry_number = int(command)
            if entry_number > 0:
                sell_item(entry_number)
            else:
                input("Please enter a valid entry number. Press Enter to try again.")
                main_menu()
        except(ValueError):
            print("This was an invalid command. Press Enter to try again")
            main_menu()
    
def display_inventory():
    inventory = load_inventory()
    num = 0
    total_value = 0
    if inventory :
        for product in inventory :
            num += 1
            catalogue_item = Product(product['name'], product['price'], product['quantity'])
            new_line = str(num) + " - " + catalogue_item.display_inventory_stock()
            print(new_line)
            total_value += product['price'] * product['quantity']
    else :
        print("The store currently has no inventory!")
    if total_value > 0 :
        print(f"\nThe current total value of the store inventory is ${total_value}")

main_menu()
