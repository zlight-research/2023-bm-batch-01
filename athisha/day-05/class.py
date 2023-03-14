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
# Item class has two attributes item_name and item_price
class Item:
    def __init__(self, item_name, item_price):
        self.name = item_name
        self.price = item_price
    # a string representation of an Item object.
    def __str__(self):
        return f"{self.name} ({self.price})"

# Seller class has two attributes seller_name and category
class Seller:
    def __init__(self, seller_name, category):
        self.seller_name = seller_name
        self.category = category
# get_items method returns a list.
    def get_items(self):
        for category, item_list in seller_data[self.seller_name].items():
            if category == self.category:
                return [Item(item["item"], item["price"]) for item in item_list]
# Add a new item to the seller_data dictionary for a given seller and category.
    def add_item(self, item_name, item_price):
        item_data = {"item": item_name, "price": item_price}
        for category, item_list in seller_data[self.seller_name].items():
            if category == self.category:
                item_list.append(item_data) #appending item_data
                break
        else:
            # Category not found or seller rasie error
            raise ValueError(f"Category '{self.category}' not found for seller '{self.seller_name}'.")
        
# Returns the seller in each category.
    def to_list_dict(self):
        categories = seller_data[self.seller_name]
        return {category: [item for item in items] for category, items in categories.items()}
# seller_data  items sold by different sellers(best store, supreme).
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
# The specified seller_name and category
seller_name,category,item_name,item_price = input("Enter the seller name: "), input("Enter the category: "), input("Enter the item name: "),  int(input("Enter the item price: "))
# Add the new item to the seller_data
seller1 = Seller(seller_name, category)
seller1.add_item(item_name, item_price)

output = {}
# Item objects, and adding a string representation of each Item
for seller_name in seller_data.keys():
    output[seller_name] = {}
    for category in seller_data[seller_name].keys():
        seller = Seller(seller_name, category)
        items = seller.get_items()
        output[seller_name][category] = [str(item) for item in items]
# Object to the output dictionary. 
print(output)

seller_data = {}
# It should not be case-sensitive
while True:
    # User to enter the name of a new seller 
    seller_name = input("Enter the new seller name or 'quit': ")
    # User enter "quit", the loop break.
    if seller_name.lower() == "quit":
        break
    seller_data[seller_name] = {}
    while True:
        # The user enter "done", the loop break.
        category = input(f"Enter the new category or 'done': ")
        if category.lower() == "done":
            break
        # A list that is stored in seller_data
        seller_data[seller_name][category] = []
        while True:
            item_name = input(f"Enter the new item name or  'done': ")
            if item_name.lower() == "done":
                break
            item_price = int(input("Enter the new item price: "))
            seller_data[seller_name][category].append({"item": item_name, "price": item_price})
# seller_data result
print(seller_data)
# Enter your seller_name, category, item_name, item_price
seller_name, category, item_name, item_price = input("Enter the seller name: "), input("Enter the category: "), input("Enter the item name: "), int(input("Enter the item price: "))

try:
    seller1 = Seller(seller_name, category)
except KeyError:
    print(f"Seller '{seller_name}' not found.")
else:
    try:
        seller1.add_item(item_name, item_price)
    except ValueError as e: # the error message.
        print(e)
    else:
        output = {
            seller1.seller_name: {
                seller1.category: [{"item": item.name, "price": item.price} for item in seller1.get_items()]
            }
        }
        print(output)
