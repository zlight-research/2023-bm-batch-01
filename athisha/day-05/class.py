"""1. Create a class for Seller and Items with following attributes and operations
Seller class has seller name, category,  items_in_stock
items class has item_name and price.
1. Items should have default method to set the item name and price per unit

2. Seller class should have initialize operation to

2.a Set the seller name

2.b a method to add part to the list of items

2. c a function to takes the arguemtn and return the cost of the part.

2.d. a function to return the status if the item is present in the seller side, it should not be case-sensitive

seller_data = {
    "best store": {
        "fresh fruits": [{"item": "apple", "price": 50}, {"item": "orange", "price": 80}, {"item": "banana", "price": 26}],
        "vegetables": [{"item": "carrot", "price": 30}, {"item": "onion", "price": 65}, {"item": "zoya", "price": 15}]
    },
    "supreme": {
        "cakes": [{"item": "black forest", "price": 450}, {"item": "white forest", "price": 520}, {"item": "red velvet", "price": 860}],
        "drinks": [{"item": "pepsi", "price": 45}, {"item": "fanta", "price": 52}, {"item": "latte", "price": 100}]
    }
}"""

#2. Seller class should have initialize operation to

"""seller class initialize its attribute based on seller data"""
# __init__ method initialize a seller object name, category,  items_in_stock.


class Item:
    def __init__(self, item_name = "" , price = 0):
        self.name = item_name
        self.price = price 
    
    def set_item(self, item_name, price):
        self.item_name = item_name
        self.price = price

class Seller:
    def __init__(self, seller_name = "",category = "", items_in_stock = {}):
        self.seller_name = seller_name
        self. category = category
        self.items_in_stock = items_in_stock

    def add_item(self, item_name, price):
        item =Item(item_name, price)
        if self.category in self.items_in_stock:
            self.items_in_stock[self.self.category].append({"item": item.item_name, "price": item.price})
        else:
            self.items_in_stock[self.self.category]=[{"item": item.item_name, "price": item.price}]

    def get_cost(self, item_name):
        item_name = item_name.lower()
        if self.category in self.items_in_stock:
            for item in self.items_in_stock[self.category]:
                if item["item"].lower() == item_name:
                    return item
        return "Item not found"

    def is_item_present(self,item_name):
        item_name = item_name.lower()
        