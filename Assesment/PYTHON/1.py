# Fruit Store  Application with Calculator
#first to define menu with def
def display_menu():
    print("Welcome to the Fruit Store!")
    print("1. View available fruits")
    print("2. Add a fruit to the cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")
#then define fruits available
def view_fruits():
    print("Available fruits:")
    print("- Apple    = 30 per kg")
    print("- Banana   = 40 per kg")
    print("- Orange   = 50 per kg")
    print("- Mango    = 30 per kg")
#then define the cart using def 
def add_to_cart(cart):
    fruit = input("Enter the fruit name: ")
    quantity = float(input("Enter the quantity in kg: "))
    cart[fruit] = quantity
    print(f"{quantity} kg of {fruit} added to the cart.")
#last define cart view which fruits had been selected
def view_cart(cart):
    print("Items in your cart:")
    for fruit, quantity in cart.items():
        print(f"- {fruit}: {quantity} kg")
#finally define checkout and to calculate the cost of purchase
def checkout(cart):
    print("Checking out...")
    total_cost = 0
    for fruit, quantity in cart.items():
        if fruit == "Apple":
            price_per_kg = 30
        elif fruit == "Banana":
            price_per_kg = 40
        elif fruit == "Orange":
            price_per_kg = 50
        elif fruit == "Mango":
            price_per_kg = 30
        else:
            price_per_kg = 0
#ths is to calculate the cost
from controller import calculation
calculation()
#finaly print the total cost
def fruit_store():
    cart = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_fruits()
        elif choice == '2':
            add_to_cart(cart)
        elif choice == '3':
            view_cart(cart)
        elif choice == '4':
            checkout(cart)
            break
        elif choice == '5':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the fruit store application
fruit_store()
