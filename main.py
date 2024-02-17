import json
from pyfiglet import Figlet

class CoffeeShop:
    def __init__(self):
        self.data = {'orders': [], 'users': [], 'groups': []}
        self.menu = [
            {"name": "Coffee", "price": 3.00, "additional": "sugar", "additional_price": 0.50},
            {"name": "Tea", "price": 1.50},
            {"name": "Hot Chocolate", "price": 4.00},
            {"name": "Tuna Sandwich", "price": 3.49},
            {"name": "Beef Sandwich", "price": 4.00},
            {"name": "Turkey Sandwich", "price": 6.50}
        ]
        self.max_group_orders = 5
        self.current_user = None

    def logoOutput(self):
        f = Figlet(font="small")
        print(f.renderText("Hmaidi's Coffee Shop"))
    
    def load_users(self):
        try:
            with open("users.json", "r") as file:
                data = file.read()
                if data:
                    self.data['users'] = json.loads(data)
                else:
                    self.data['users'] = []
        except FileNotFoundError:
            with open("users.json", "w") as file:
                json.dump([], file)
    
    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.data['users'], file)

    def login(self):
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            name = input("Enter your name: ").capitalize()
            password = input("Enter your password: ")
            
            for user in self.data['users']:
                if user['name'].lower() == name.lower() and user['password'] == password:
                    self.current_user = user
                    print("\nHello {}, Welcome back to Hmaidi's Coffee Shop\n".format(user['name']))
                    return True
            
            attempts += 1
            trials_left = max_attempts - attempts
            if trials_left > 0:
                print("Invalid username or password. You have", trials_left, "attempt(s) left.")
            else:
                print("No more attempts left. Please try again later.")
        
        return False

    
    def register(self):
        print("Create a new account")
        name = input("Enter your name: ").capitalize()
        postcode = input("Enter Your postcode: ")
        houseNumber = input("Enter Your House Number, {}: ".format(name))
        password = input("Enter a password: ")
        self.data['users'].append({'name': name, 'postcode': postcode, 'houseNumber': houseNumber,
                                    'password': password})
        self.save_users()
        print("\nAccount created successfully!\n")
        return True

    def userOptions(self):
        print("\n1. Place an Order")
        print("2. View Past Invoices")
        print("3. Logout")
        option = input("\nSelect an option: ")
        if option == '1':
            self.placeOrder()
        elif option == '2':
            self.viewInvoices()
        elif option == '3':
            print("Logging out...")
            self.current_user = None
            return
        else:
            print("Invalid option. Please select a valid option.")


    def display_menu(self):
        print("\nHere is our whole menu")
        for n, item in enumerate(self.menu, 1):
            print("\n{}. {}: £{}".format(n, item['name'], item['price']))

    
    def placeOrder(self):
        order_details = {'items': []}
        
        print("\nHere is our whole menu:")
        for i, item in enumerate(self.menu):
            print("{}. {}: £{:.2f}".format(i + 1, item['name'], item['price']))

        while True:
            order = int(input("\nUse the number to select the order: (Enter 0 to finish order processing): "))
            
            if order == 0:
                break

            if order < 1 or order > len(self.menu):
                order = int(input("Enter a number between 1 and {} only: ".format(len(self.menu))))

            selected_item = self.menu[order - 1]['name']
            item_price = self.menu[order - 1]['price']

            print("You have selected menu option {}: {}".format(order, selected_item))
            quantity = int(input("How many of these would you like: "))
            
            total_price = quantity * item_price
            print("Total price: £{:,.2f}".format(total_price))

            if order == 1 or order == 2:
                sugar_preference = input("Would you like some sugar? (y/n): ")
                if sugar_preference.lower() == "y":
                    sugar_price = 0.50
                    total_price += sugar_price * quantity
                    selected_item += " with Sugar"

            order_details['items'].append({'item': selected_item, 'quantity': quantity, 'total_price': total_price})

        print("\nOrder placed successfully! Saving receipt...")
        self.receipt(order_details)
        print("Receipt saved as receipt.txt")

        with open("receipt.txt", "r") as file:
            receipt_content = file.readlines()[-16:]
            print("\n".join(receipt_content))

    def receipt(self, order_details):
        with open("receipt.txt", "a") as file:
            file.write("\nInvoice for {}".format(self.current_user['name']))
            file.write("----------------------------------------------\n")
            file.write("Name: {}".format(self.current_user['name']))
            file.write("Postcode: {}".format(self.current_user['postcode']))
            file.write("House Number: {}".format(self.current_user['houseNumber']))
            file.write("----------------------------------------------\n")

            if order_details:
                file.write("{:<20} {:<10} {:<15}\n".format("Item", "Quantity", "Total Price"))
                file.write("----------------------------------------------\n")
                for item in order_details['items']:
                    name = item['item']
                    quantity = item['quantity']
                    total_price = round(item['total_price'], 2)
                    file.write("{:<20} {:<10} {:<15}\n".format(name, quantity, total_price))

                subtotal = sum(item['total_price'] for item in order_details['items'])
                vat = subtotal * 0.2
                total_amount = subtotal + vat

                file.write("----------------------------------------------\n")
                file.write("{:<30} £{:,.2f}".format("Subtotal:", subtotal))
                file.write("{:<30} £{:,.2f}".format("VAT (20%):", vat))
                file.write("{:<30} £{:,.2f}".format("Total Amount:", total_amount))

        print("\nReceipt saved successfully.")

    def viewInvoices(self):
        if self.current_user:
            current_user_info = {
                'name': self.current_user['name'],
                'postcode': self.current_user['postcode'],
                'houseNumber': self.current_user['houseNumber']
            }
            try:
                with open("receipt.txt", "r") as file:
                    past_invoices = file.read().split('\n\n')
                    user_invoices = []
                    for invoice in past_invoices:
                        if all(info in invoice for info in current_user_info.values()):
                            user_invoices.append(invoice)
                    if user_invoices:
                        print("\nPast Invoices for {}:\n".format(current_user_info['name']))
                        for invoice in user_invoices:
                            print(invoice)
                    else:
                        print("No past invoices found for {}.".format(current_user_info['name']))
            except FileNotFoundError:
                print("\nNo past invoices found for {}.".format(current_user_info['name']))
        else:
            print("Please login first to view invoices.")

    def run(self):
        self.logoOutput()
        self.load_users()
        logged_in = False
        print("\nWelcome to Hmaidi`s Coffee Shop")

        while True:
            if not logged_in:
                print("1. Login")
                print("2. Register")
                print("4. Exit")
                choice = input("\nChoose an option: ")
                if choice == '1':
                    self.login()
                    if self.current_user:
                        logged_in = True
                elif choice == '2':
                    if self.register():
                        continue
                elif choice == '4':
                    break
            else:
                print("\nWhat would you like to do?")
                print("1. Place an Order")
                print("2. View Past Invoices")
                print("3. Logout")
                print("4. Exit")
                option = input("\nSelect an option: ")
                if option == '1':
                    self.placeOrder()
                elif option == '2':
                    self.viewInvoices()
                elif option == '3':
                    print("Logging out...")
                    logged_in = False
                elif option == '4':
                    break

if __name__ == "__main__":
    coffee_shop = CoffeeShop()
    coffee_shop.run()
    print("Thank you for visiting Hmaidi's Coffee Shop")
