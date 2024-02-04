from pyfiglet import Figlet

"""
Complete validation e.g. only let items choose quantity between 1 and 10 or ensure names inputs have a value entered in them
Add while loop to repeat for another order line
Add 1d Arrays to all variables like the video.
Add password code here
"""

def logoOutput():
    f = Figlet(font="big")
    print(f.renderText("Hmaidi`s Coffee Shop"))

def createOrder(item, price, quantity, postCode, Total, menu):
    print("Welcome to Hmaidi`s Coffee Shop Customer")
    name = ""

    while name == "":
        name = input("Please Enter Your name: ")

    while True:
        postCode = input("Please Enter Your postcode: ")

        if postCode == "":
            postCode = input("Please Enter a postcode! ")
        else:
            break

    while True:
        Doornumber = input(f"Please enter your door number {name}")

        if Doornumber == "":
            Doornumber = input("Please you have to enter a door number")
        else:
            break

    print("Here is our whole menu")
    print("Welcome to Hmaidi`s Coffee Shop Customer")
    print("Here is our whole menu")

    for i in menu:
        print(i)

    while True:
        orderSelection = int(input("Use the number to select the order "))

        if orderSelection < 1 or orderSelection > 6:
            orderSelection = input("Enter a number between 1 and 6 only")

        if orderSelection == 1:
            print("You have selected a coffee")
            quantity = int(input("How many of these would you like"))
            price = 3.00
            item = "Coffee"
            sugar_preference = input(f"Would you like sugar with your {item} for 50p extra (yes/no):")

            if sugar_preference.lower() == "yes":
                print(f"Sugar will be added to your {item}.")
                price = 3.50
            elif sugar_preference.lower() == "no":
                print(f"No sugar will be added to your {item}")
        elif orderSelection == 2:
            print("You have selected a Tea.")
            quantity = int(input("How many would of these would you like"))
            price = 1.50
            item = "Tea"
        elif orderSelection == "3":
            print("You have selected a Hot Chocolate")
            quantity = int(input("How many of these would you like"))
            price = 4.00
            item = "Hot Chocolate"
        elif orderSelection == "4":
            print("You have selected a Tuna Sandwich")
            price = 3.49
        elif orderSelection == "5":
            print("You have selected a beef sandwich")
            price = 4.00
        elif orderSelection == "6":
            print("You have selected a Turkey Sandwich")
            price = 6.50

        Total = price * quantity

        print()
        print("Reciept")
        print("----------------------------------------------")
        print(f"Item Ordered:    {item}")
        print(f"Price:       £{price}")
        print(f"Quantity:    {quantity}")
        print(f"Total:       £{Total}")
        print(f"postCode:    {postCode}")
        print(f"Doornumber:  {Doornumber}")

# Complete validation e.g. only let items choose quantity between 1 and 10 or ensure names inputs have a value entered in them
# Declare all variables here

Total = 0
menu = ["1.Coffee 3.00", "2.Tea 1.50", "3.Hot Chocolate 4.00", "4. Tuna Sandwich 3.49", "5.Beef Sandwich 4.00", "6. Turkey Sandwich 6.50"]
item = ""
price = 0
quantity = 0
postCode = ""
Doornumber = 0
logoOutput()
createOrder(item, price, quantity, postCode, Total, menu)

