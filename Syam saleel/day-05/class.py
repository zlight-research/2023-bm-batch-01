
class Item:
    def __init__(self):
        self.item_name = "No item name set"
        self.price = 0
        
    def set_details(self, item_name, price):
        self.item_name = item_name
        self.price = price
        
class Seller:
    def __init__(self, seller_name, category):
        self.seller_name = seller_name
        self.category = category
        self.items_in_stock = []
    def add_item(self, item):
        self.items_in_stock.append(item)