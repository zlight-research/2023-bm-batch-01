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



# seller_data = {
#     "best store": {
#         "fresh fruits": [{"item": "apple", "price": 50}, {"item": "orange", "price": 80}, {"item": "banana", "price": 26}],
#         "vegetables": [{"item": "carrot", "price": 30}, {"item": "onion", "price": 65}, {"item": "zoya", "price": 15}]
#     },
#     "supreme": {
#         "cakes": [{"item": "black forest", "price": 450}, {"item": "white forest", "price": 520}, {"item": "red velvet", "price": 860}],
#         "drinks": [{"item": "pepsi", "price": 45}, {"item": "fanta", "price": 52}, {"item": "latte", "price": 100}]
#     }
# }


# class Items:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     def item_details(self):
#         # self.name = name
#         # self.price = price
#         print(self.name)

# class Seller:
#     def _init_(self,seller_name,category,items_in_stock):
#         self.seller_name = seller_name
#         self.category = category
#         self.items_in_stock = items_in_stock

#     def add_item(self, category, items_in_stock):
#         if category not in self.items_in_stock:
#             self.items_in_stock[category] = []
#             self.items_in_stock[category].append(items_in_stock)

# z = Items('',500).item_details()

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


class Items:
    def __init__(self):
        self.item_name = "Default item"
        self.price_per_unit = 0

    def set_item_details(self, item_name, price_per_unit):
        self.item_name = item_name
        self.price_per_unit = price_per_unit


class Seller:
    def __init__(self, seller_name, category):
        self.seller_name = seller_name
        self.category = category
        self.items_in_stock = []

    def add_item(self, item_name, price_per_unit):
        new_item = Items()
        new_item.set_item_details(item_name, price_per_unit)
        self.items_in_stock.append(new_item)

    def get_item_cost(self, item_name):
        for item in self.items_in_stock:
            if item.item_name.lower() == item_name.lower():
                return item.price_per_unit
        return "Item not found in stock."

    def is_item_in_stock(self, item_name):
        for item in self.items_in_stock:
            if item.item_name.lower() == item_name.lower():
                return "Item is present in stock."
        return "Item is not present in stock."

# Create item in the seller_data dictionary
seller_objs = {}


for seller_name, seller_data in seller_data.items():
    seller_objs[seller_name] = Seller(seller_name, "")
    for category, items in seller_data.items():
        seller_objs[seller_name].category = category
        for item in items:
            item_name = item['item']
            price_per_unit = item['price']
            seller_objs[seller_name].add_item(item_name, price_per_unit)

print(seller_objs['best store'].get_item_cost('apple'))  # Output: 50
# Item is present in stock.
print(seller_objs['best store'].is_item_in_stock('Carrot'))
# Item is present in stock.
print(seller_objs['supreme'].is_item_in_stock('pepsi'))
# Item is not present in stock.
print(seller_objs['supreme'].is_item_in_stock('ice cream'))

key = input("Enter a key: ")
if key in seller_data:
    print(seller_data[key])
else:
    print("Key not found")

