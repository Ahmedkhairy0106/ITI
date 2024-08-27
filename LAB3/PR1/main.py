"""
# 26/8/2024 form 8 to 11 pm
# ITI
"""

from oop import *

shopping_card = ShopCard()

while True:
    print("\nWelcome In My Store \n--------------------\n")
    print("Please Enter The Operation Number To Perform It: \n1. Add Product.\n2. Display All Products\n3. Remove Product.\n4. Clear Cart.\n5. Calculate Total Price.")

    operation = input()
    if operation not in ['1', '2', '3', '4', '5']:
        print("Invalid action. Please try again.")
        continue

    if operation == "1":
        pname = input("Enter Product Name: ").capitalize()
        while not pname.isalpha():
            print("Invalid input. Product name should only contain alphabetic characters.")
            pname = input("Enter Product Name: ").capitalize()

        price = input("Enter Product Price: ")  # Correct input for price
        while True:
            try:
                price = float(price)
                if price < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Product price should be a positive number.")
                price = input("Enter Product Price: ")

        quantity = input("Enter Product Quantity: ")  # Correct input for quantity
        while True:
            try:
                quantity = int(quantity)
                if quantity < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Product quantity should be a non-negative integer.")
                quantity = input("Enter Product Quantity: ")

        product = Product(pname, price)
        shopping_card.add_product(product, quantity)  # Use the instance to add product

    elif operation == "2":
        try:
            if not shopping_card.products_list:
                print("Shopping Card is empty")
            else:
                for pname, details in shopping_card.products_list.items():
                    print(f"Product Name: {pname}, Price: {details['price']}, Quantity: {details['Quantity']}")
        except AttributeError:
            print("There Are No Products To Display.")

    elif operation == "3":
        n = input("Enter The Product Name You Need To Del From Shopping Cart: ").capitalize()
        while not n.isalpha():
            print("Invalid input. Product name should only contain alphabetic characters.")
            n = input("Enter Product Name: ").capitalize()
        if n in shopping_card.products_list:
            shopping_card.remove_product(n)
            print(f"Product '{n}' has been removed from the shopping cart.")
        else:
            print(f"Product '{n}' not found in the shopping cart.")

    elif operation == "4":
        shopping_card.clear_cart()
        print("The Cart Has Been Successfully Cleared.")

    elif operation == "5":
        total_price = 0
        for pname, details in shopping_card.products_list.items():
            print(f"Your Products:\nProduct Name: {pname}, Price: {details['price']}, Quantity: {details['Quantity']}")
            total_price += details['price'] * details['Quantity']
        if total_price == 0:
            print("No Product In The Shopping Cart.")
        else:
            print("Your total Price is:", total_price)