"""1. Create a class for Seller and Items with following attributes and operations
Seller class has seller name, category,  items_in_stock
items class has item_name and price.
1. Items should have default method to set the item name and price per unit"""

class Seller:
    def __init__(self,name,category,items_in_stock):
        self.name=name
        self.category=category
        self.items_in_stock=items_in_stock
    def add_item(self,item):
        self.items_in_stock.append(item)
    def remove_item(self,item):
        self.items_in_stock.remove(item)


class Item:
    def __init__(self,item_name,price):
        self.name=item_name
        self.category=price
    def set_name(self,name):
        self.name=name
    def set_name(self,price):
        self.name=price


        