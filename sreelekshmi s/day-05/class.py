"""
1. Create a class for Seller and Items with following attributes and operations
Seller class has seller name, category,  items_in_stock
items class has item_name and price.
1. Items should have default method to set the item name and price per unit



2. Seller class should have initialize operation to

2.a Set the seller name (a method to create new seller)

2.b a method to add part to the list of items

2. c a function to take the argument and return the cost of the part.

2.d. a function to return the status if the item is present in the seller side, it should not be case-sensitive



seller_data = {
        "best store": {
            "fresh fruits": [{"item":"apple","price": 50}, {"item":"orange","price":80}, {"item":"banana","price":26}],
            "vegetables": [{"item":"carrot","price":30}, {"item":"onion","price":65}, {"item":"zoya","price":15}]
        },
        "supreme": {
            "cakes": [{"item":"black forest","price":450}, {"item":"white forest","price":520}, {"item":"red velvet","price":860}],
            "drinks": [{"item":"pepsi","price":45}, {"item":"fanta","price":52}, {"item":"latte","price":100}]
        }
    }
"""

class Items:
    def __init__(self, item_name=str, price=int):
        self.item_name = item_name
        self.price = price

    def set_item(self, item_name, price):
        self.item_name = item_name
        self.price = price


class Seller:
    def __init__(self, seller_name,category,items_in_stock):
        self.seller_name = seller_name
        self.category = category
        self.items_in_stock = items_in_stock

    