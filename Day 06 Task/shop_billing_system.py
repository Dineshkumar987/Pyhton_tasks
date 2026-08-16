# Shop Billing System

products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

categories = {"Stationery"}

# Product details using tuples
product_details = {
    "Pen": ("Stationery", 10),
    "Notebook": ("Stationery", 50),
    "Pencil": ("Stationery", 5)
}

cart = []

# Recursive function to calculate total bill
def total_bill(cart, index=0):
    if index == len(cart):
        return 0

    item = cart[index]

    if not isinstance(item, tuple):
        raise TypeError

    product, quantity = item

    return (products[product] * quantity) + total_bill(cart, index + 1)

# Display products
def display_products():
    print("\nAvailable Products:")
    for product, price in products.items():
        print(product, ":", price)
    print()

# Add item to cart
def add_to_cart():
    try:
        product = input("Enter product name: ")

        if product not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        cart.append((product, quantity))
        print("Item added to cart successfully.\n")

    except ValueError:
        print("Invalid quantity! Please enter a number.\n")
    except NameError:
        print("Product not found in store.\n")

# View total bill
def view_bill():
    try:
        if not isinstance(cart, list):
            raise TypeError

        total = total_bill(cart)

        # Only to demonstrate ZeroDivisionError handling
        if len(cart) == 0:
            raise ZeroDivisionError

        print("\nItems in Cart:")
        for product, quantity in cart:
            print(product, "x", quantity)

        print("Total Bill:", total)
        print()

    except TypeError:
        print("Cart data type error.\n")
    except ZeroDivisionError:
        print("Calculation error: division by zero.\n")

# Main Menu
while True:
    print("1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_bill()
    elif choice == "4":
        print("Program Exited.")
        break
    else:
        print("Invalid choice.\n")