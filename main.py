from pyfiglet import Figlet

class CoffeeShop:
    def __init__(self):
        self.data = {'orders': []}
        self.menu = [
        {"name": "Coffee", "price": 3.00, "additional": "sugar", "additional_price": 0.50},
        {"name": "Tea", "price": 1.50},
        {"name": "Hot Chocolate", "price": 4.00},
        {"name": "Tuna Sandwich", "price": 3.49},
        {"name": "Beef Sandwich", "price": 4.00},
        {"name": "Turkey Sandwich", "price": 6.50}
    ]

    def logoOutput(self):
        f = Figlet(font="small")
        print(f.renderText("Hmaidi`s Coffee Shop"))

    def userDetails(self):
        name = input("Enter your name: ").capitalize()
        postcode = input("Enter Your postcode: ")
        houseNumber = input("Enter Your House Number, {}: ".format(name))
        self.data['name'] = name
        self.data['postcode'] = postcode
        self.data['houseNumber'] = houseNumber
        self.data['orders'] = []
        print()
        print("Hello {}, Welcome to Hmaidi`s Coffee Shop".format(name))
    
    def display_menu(self):
        print("\nHere is our whole menu")

        for n, item in enumerate(self.menu, 1):
            print("{}. {}: £{}".format(n, item['name'], item['price']))

    def orderSelection(self):
        while True:
            print()
            order = int(input("Use the number to select the order: (Enter 0, to finish order processing): "))

            if order == 0:
                break

            if order < 1 or order > len(self.menu):
                order = int(input("Enter a number between 1 and {} only: ".format(len(self.menu))))

            selected_item = self.menu[order - 1]['name']
            item_price = self.menu[order - 1]['price']

            print("You have selected menu option{}:, {}".format(order, selected_item))
            quantity = int(input("How many of these would you like: "))
            total_price = quantity * item_price
            print("Total price: {:,.2f} ".format(total_price))

            if order == 1 or order == 2:
                sugar_preference = input("Would you like some sugar? (y/n): ")
                if sugar_preference.lower() == "y":
                    sugar_price = 0.50
                else:
                    sugar_price = 0.0
                total_price = (item_price + sugar_price) * quantity
            
            self.data['orders'].append({'item': selected_item, 'quantity': quantity, 'total_price': total_price})

    def receipt(self):
        print()
        with open("receipt.txt", "a") as file:

            file.write("\nInvoice for {}\n".format(self.data['name']))
            file.write("----------------------------------------------\n")
            file.write("Name: {}\n".format(self.data['name']))
            file.write("Postcode: {}\n".format(self.data['postcode']))
            file.write("House Number: {}\n".format(self.data['houseNumber']))
            file.write("----------------------------------------------\n")

            if self.data['orders']:
                file.write("{:<20} {:<10} {:<15}\n".format("Item", "Quantity", "Total Price"))
                file.write("----------------------------------------------\n")
                for order_details in self.data['orders']:
                    item = order_details['item']
                    quantity = order_details['quantity']
                    total_price = round(order_details['total_price'], 2)
                    file.write("{:<20} {:<10} {:<15}\n".format(item, quantity, total_price))

                subtotal = sum(order['total_price'] for order in self.data['orders'])
                vat = subtotal * 0.2
                total_amount = subtotal + vat

                file.write("----------------------------------------------\n")
                file.write("{:<30} £{:,.2f}\n".format("Subtotal:", subtotal))
                file.write("{:<30} £{:,.2f}\n".format("VAT (20%):", vat))
                file.write("{:<30} £{:,.2f}\n".format("Total Amount:", total_amount))

        with open("receipt.txt", "r") as file:
            receipt_content = file.read()
            print(receipt_content)

    def run(self):
        self.logoOutput()
        self.userDetails()
        while True:
            self.display_menu()
            self.orderSelection()
            self.receipt()

            second_order = input("Do you want to place another order? (y/n): ")
            if second_order.lower() != "y":
                break

coffee_shop = CoffeeShop()
coffee_shop.run()

print("Thank you for your order")
        
