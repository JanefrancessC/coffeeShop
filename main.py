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
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            
            for user in self.data['users']:
                if user['name'].lower() == name.lower() and user['password'] == password:
                    self.data['name'] = user['name']
                    self.data['postcode'] = user['postcode']
                    self.data['houseNumber'] = user['houseNumber']
                    print("\nHello {}, Welcome back to Hmaidi's Coffee Shop\n".format(user['name']))
                    return
            
            attempts += 1
            trials_left = max_attempts - attempts
            if trials_left > 0:
                print("Invalid username or password. You have", trials_left, "attempt(s) left.")
            else:
                print("No more attempts left. Please try again later.")

    
    def register(self):
        print("Create a new account")
        name = input("Enter your name: ").capitalize()
        postcode = input("Enter Your postcode: ")
        houseNumber = input("Enter Your House Number, {}: ".format(name))
        password = input("Enter a password: ")
        self.data['users'].append({'name': name, 'postcode': postcode, 'houseNumber': houseNumber,
                                    'password': password})
        self.save_users()
        print("Account created successfully!")

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
        for i, item in enumerate(self.menu, 1):
            print("{}. {}: £{:.2f}".format(i, item['name'], item['price']))

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
            file.write("\nInvoice for {}\n".format(self.data.get('name', 'Unknown')))
            file.write("----------------------------------------------\n")
            file.write("Name: {}\n".format(self.data.get('name', 'Unknown')))
            file.write("Postcode: {}\n".format(self.data.get('postcode', 'Unknown')))
            file.write("House Number: {}\n".format(self.data.get('houseNumber', 'Unknown')))
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
                file.write("{:<30} £{:,.2f}\n".format("Subtotal:", subtotal))
                file.write("{:<30} £{:,.2f}\n".format("VAT (20%):", vat))
                file.write("{:<30} £{:,.2f}\n".format("Total Amount:", total_amount))

        print("\nReceipt saved successfully.")


    def viewInvoices(self):
        current_user_info = {
            'name': self.data.get('name', 'Unknown'),
            'postcode': self.data.get('postcode', 'Unknown'),
            'houseNumber': self.data.get('houseNumber', 'Unknown')
        }
        try:
            with open("receipt.txt", "r") as file:
                past_invoices = file.read().split('\n\n')
                if past_invoices:
                    print("\nPast Invoices for {}:\n".format(current_user_info['name']))
                    for invoice in past_invoices:
                        if all(info in invoice for info in current_user_info.values()):
                            print(invoice)
                    if not any(info in invoice for info in current_user_info.values() for invoice in past_invoices):
                        print("No past invoices found for {}.".format(current_user_info['name']))
                else:
                    print("\nNo past invoices found for {}.".format(current_user_info['name']))
        except FileNotFoundError:
            print("\nNo past invoices found for {}.".format(current_user_info['name']))



    def run(self):
        self.logoOutput()
        self.load_users()
        logged_in = False
        print("\nWelcome to Hmaidi`s Coffee Shop")

        while True:
            if not logged_in:
                print("1. Login")
                print("2. Register")
            else:
                print("\nWhat would you like to do?:")
                print("1. Place an Order")
                print("2. View Past Invoices")
                print("3. Logout")
            print("4. Exit")
            choice = input("\nChoose an option: ")
            if choice == '1' and not logged_in:
                self.login()
                if 'name' in self.data:
                    logged_in = True  
            elif choice == '1' and logged_in:
                self.placeOrder()
            elif choice == '2' and logged_in:
                self.viewInvoices()
            elif choice == '3' and logged_in:
                logged_in = False  
            elif choice == '4':
                break


if __name__ == "__main__":
    coffee_shop = CoffeeShop()
    coffee_shop.run()
    print("Thank you for visiting Hmaidi's Coffee Shop")

