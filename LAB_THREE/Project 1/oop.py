"""
# 26/8/2024 form 8 to 11 pm
# ITI
"""
class Product:
    def __init__(self, pname, price):
        self.pname = pname
        self.price = price

class ShopCard:
    def __init__(self):
        self.products_list = {}

    def add_product(self, product, quantity):
        self.products_list[product.pname] = {"price": product.price, "Quantity": quantity}
        print(f"Product '{product.pname}' added to shopping card with quantity {quantity}")
        print("--------------------------------------------------")
        return self.products_list[product.pname]

    def display_product(self):
        return self.products_list

    def remove_product(self,n):
        if n in self.products_list:
            del self.products_list[n]

    def clear_cart(self):
        del self.products_list
