class Seller:
    def __init__(self, seller_name,category,items_in_stock):
        self.seller_name = seller_name
        self.category=category
        self.items_in_stock={}

    def add_item(self, category, item):
        if category not in self.items_in_stock:
            self.items_in_stock[category]=[]
        self.items_in_stock[category].append(item)

    def get_cost(self, item_name):
        for category, items in self.items_in_stock.items():
            for item in items:
                if item.item_name.lower() == item_name.lower():
                    return item.price
        return None

"""def has_item(self, item_name):
        for category, items in self.items_in_stock.items():
            for item in items:
                if item.item_name.lower() == item_name.lower():
                    return True
        return False"""


class Items:
    def __init__(self, item_name=None, price=0):
        self.item_name = item_name
        self.price = price

    def set_details(self, name, price):
        self.item_name = name
        self.price = price


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

sellers = {}

while True:
    seller_name = input("Enter seller name : ")
    if not seller_name:
        break
    seller = Seller(seller_name)
    while True:
        category = input("Enter item category : ")
        if not category:
            break
        while True:
            item_name = input("Enter item name : ")
            if not item_name:
                break
            item_price = input("Enter item price : ")
            item_obj = Items()
            item_obj.set_details(item_name, int(item_price))
            seller.add_item(category, item_obj)
    sellers[seller_name] = seller

# Print the items for each seller
for seller_name, seller in sellers.items():
    print(f"Seller: {seller_name}")
    for category, items in seller.items_in_stock.items():
        print(f"Category: {category}")
        for item in items:
            print(f"Item: {item.item_name} | Price: {item.price}")
