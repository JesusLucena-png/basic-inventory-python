# List where the products will be stored
products = []

# Variable to control the loop
running = True

while running:

    print("\033[34m INVENTARIO \033[0m".center(70, "-"))

    try:
        # Ask for the product name
        name = input("\n\033[34m >> \033[0mEnter Product Name : ")

        # Ask for the unit price of the product
        price = float(input("\n\033[34m >> \033[0mEnter Unit Product Price : "))

        # Ask for the total quantity
        quantity = int(input("\n\033[34m >> \033[0mEnter Total Product Quantity : "))

    except ValueError:
        # If the user enters an invalid value
        print("\n\033[1;31m" + "-"*60)
        print("Error: Invalid Value")
        print("-"*60 + "\033[0m")

        continue

    # Calculate total cost
    total_cost = price * quantity

    # Save the product in the list as a dictionary
    products.append({
        "Name": name,
        "Price": price,
        "Quantity": quantity
    })

    # Display the product information and the total cost
    print("\n\033[1;32m" + "-"*60)
    print(f"Product: {name} | Price: {price} | Quantity: {quantity} | Total: {total_cost}")
    print("-"*60 + "\033[0m")

    # Stop the loop
    running = False

# -------------------------------------------------------------
# General Program Description
# This program allows the user to register a product in a simple
# inventory system. The user enters the product name, unit price,
# and quantity. The program validates that the price and quantity
# are numeric values. If an invalid value is entered, the program
# shows an error message and asks for the data again. Once the
# data is valid, the program calculates the total cost by
# multiplying the price by the quantity and then displays the
# product information and the calculated total in the console.
# -------------------------------------------------------------