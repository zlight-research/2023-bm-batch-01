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
    def __init__(self, item_name, item_price):
        self.name = item_name
        self.price = item_price

    def __str__(self):
        return f"{self.name} ({self.price})"


class Seller:
    def __init__(self, seller_name, category):
        self.seller_name = seller_name
        self.category = category

    def get_items(self):
        for category, item_list in seller_data[self.seller_name].items():
            if category == self.category:
                return [Item(item["item"], item["price"]) for item in item_list]

    def add_item(self, item_name, item_price):
        item_data = {"item": item_name, "price": item_price}
        for category, item_list in seller_data[self.seller_name].items():
            if category == self.category:
                item_list.append(item_data)
                break

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


seller_name = input("Enter the seller name: ")
category = input("Enter the category: ")
item_name = input("Enter the item name: ")
item_price = int(input("Enter the item price: "))

seller1 = Seller(seller_name, category)
seller1.add_item(item_name, item_price)

output = {
    seller_name: {
        category: [{"item": item.name, "price": item.price} for item in seller1.get_items()]
    }
}


print("Complete All seller data:")
for seller, categories in seller_data.items():
    print(f"{seller}:")
    for category, items in categories.items():
        print(f"\t{category}:")
        for item in items:
            print(f"\t\t{item['item']}: {item['price']}")

