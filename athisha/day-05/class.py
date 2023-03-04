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

    def __str__(self):
        return f"{self.name} ({self.price})"


class Seller:
    def __init__(self, name):
        self.name = name
        self.categories = {}

    def add_item(self, category, item):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(item)

    def __str__(self):
        return f"{self.name}: {len(self.categories)} categories, {sum(len(items) for items in self.categories.values())} items"

# Initialize seller data
seller_data = {
    "best store": Seller("best store"),
    "supreme": Seller("supreme")
}

seller_data["best store"].add_item("fresh fruits", Item("apple", 50))
seller_data["best store"].add_item("fresh fruits", Item("orange", 80))
seller_data["best store"].add_item("fresh fruits", Item("banana", 26))
seller_data["best store"].add_item("vegetables", Item("carrot", 30))
seller_data["best store"].add_item("vegetables", Item("onion", 65))
seller_data["best store"].add_item("vegetables", Item("zoya", 15))

seller_data["supreme"].add_item("cakes", Item("black forest", 450))
seller_data["supreme"].add_item("cakes", Item("white forest", 520))
seller_data["supreme"].add_item("cakes", Item("red velvet", 860))
seller_data["supreme"].add_item("drinks", Item("pepsi", 45))
seller_data["supreme"].add_item("drinks", Item("fanta", 52))
seller_data["supreme"].add_item("drinks", Item("latte", 100))


# Insert new item
seller_name,category,item_name,price = input("Enter the seller name: "),input("Enter the category: "),input("Enter the item name: "),int(input("Enter the price: "))

if seller_name not in seller_data:
    seller_data[seller_name] = Seller(seller_name)

if category not in seller_data[seller_name].categories:
    seller_data[seller_name].add_item(category, Item(item_name, price))
else:
    for item in seller_data[seller_name].categories[category]:
        if item.name == item_name:
            item.price = price
            break
    else:
        seller_data[seller_name].add_item(category, Item(item_name, price))


# Search for price
item_name = input("Enter the item name to find price: ")
found = False
for seller in seller_data.values():
    for category, items in seller.categories.items():
        for item in items:
            if item.name == item_name:
                print(f"{item_name} is available at {seller.name} in the {category} category for {item.price}")
                found = True

if not found:
    print(f"{item_name} is not available at any seller")


# Check availability
item_name = input("Enter the item name to check availability: ")
found = False
for seller in seller_data.values():
    for category, items in seller.categories.items():
        for item in items:
            if item.name == item_name:
                print(f"{item_name} is available at {seller.name} in the {category} category")
                found = True

if not found:
    print(f"{item_name} is not available")


