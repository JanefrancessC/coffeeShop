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
        postCode = input("Enter Your postcode: ")
        houseNumber = input("Enter Your House Number, {}: ".format(name))
        self.data['name'] = name
        self.data['postCode'] = postCode
        self.data['houseNumber'] = houseNumber
        print()
        print("Hello {}, Welcome to Hmaidi`s Coffee Shop".format(name))
    
    def display_menu(self):
        print("\nHere is our whole menu")

        for n, item in enumerate(self.menu, 1):
            print("{}. {}: £{}".format(n, item['name'], item['price']))



coffee_shop = CoffeeShop()
coffee_shop.logoOutput()
coffee_shop.userDetails()
coffee_shop.display_menu()
        
