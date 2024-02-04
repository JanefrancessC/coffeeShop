from pyfiglet import Figlet

class CoffeeShop:
    def __init__(self):
        self.data = {}
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
        print()
        print("Hello {}, Welcome to Hmaidi`s Coffee Shop".format(name))
    
    def display_menu(self):
        print("\nHere is our whole menu")

        for n, item in enumerate(self.menu, 1):
            print("{}. {}: £{}".format(n, item['name'], item['price']))

    def orderSelection(self):
        print()
        order = int(input("Use the number to select the order: "))

        if order < 1 or order > len(self.menu):
            order = int(input("Enter a number between 1 and {} only: ".format(len(self.menu))))

        selected_item = self.menu[order-1]['name']
        item_price = self.menu[order-1]['price']

        print("You have selected order: {} {}".format(order, selected_item))
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
            self.data['order'] = {'item': selected_item, 'quantity': quantity, 'total_price': total_price}
        
        self.data['order'] = {'item': selected_item, 'quantity': quantity, 'total_price': total_price}

    def receipt(self):
        print()
        print("Receipt for {}".format(self.data['name']))
        print("----------------------------------------------")
        print("Name: {}".format(self.data['name']))
        print("Postcode: {}".format(self.data['postcode']))
        print("House Number: {}".format(self.data['houseNumber']))

        order_details = self.data['order']
        print("\nOrder Details:")
        print("Item: {}".format(order_details['item']))
        print("Quantity: {}".format(order_details['quantity']))
        print("Total Price: {}".format(order_details['total_price']))



coffee_shop = CoffeeShop()
coffee_shop.logoOutput()
coffee_shop.userDetails()
coffee_shop.display_menu()
coffee_shop.orderSelection()
coffee_shop.receipt()
        
