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

seller_data = {
    "best store": {
        "fresh fruits": [{"item": "apple", "price": 50}, {"item": "orange", "price": 80}, {"item": "banana", "price": 26}],
        "vegetables": [{"item": "carrot", "price": 30}, {"item": "onion", "price": 65}, {"item": "zoya", "price": 15}]
    },
    "supreme": {
        "cakes": [{"item": "black forest", "price": 450}, {"item": "white forest", "price": 520}, {"item": "red velvet", "price": 860}],
        "drinks": [{"item": "pepsi", "price": 45}, {"item": "fanta", "price": 52}, {"item": "latte", "price": 100}]
    }
}

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Seller:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.items_in_stock = []

    def add_item(self, item_name, price):
        self.items_in_stock.append(Item(item_name, price))
        
    def get_cost(self, item_name):
        item = self.get_item(item_name)
        return item.price if item else None

    def get_item(self, item_name):
        return next((item for item in self.items_in_stock if item.name.lower() == item_name.lower()), None)

seller_name = input("Enter the name of the seller: ")
category_name = input("Enter the name of the category: ")
if (seller_data.get(seller_name) or {}).get(category_name):
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price of the item: "))
    seller = Seller(seller_name, category_name)
    seller.add_item(item_name, item_price)
    item = seller.get_item(item_name)
    cost = item.price if item else None
    has_item = bool(item)
    print(f"{seller_name} - {category_name} - {item_name}: Cost={cost}, Has Item={has_item}")
else:
    print(f"The category '{category_name}' does not exist for the seller '{seller_name}'")

