"""1. Create a class for Seller and Items with following attributes and operations
Seller class has seller name, category,  items_in_stock
items class has item_name and price.
1. Items should have default method to set the item name and price per unit"""

class Seller:
    def __init__(self, seller_name,category,items_in_stock):
        self.name=  seller_name
        self.category = category
        self.items_in_stock = items_in_stock

    def _str_(self):
        return f"{self.name}({self.category})({self.item_in_stock})"
