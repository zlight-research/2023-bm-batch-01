class Seller:

    def __init__(self, seller_name, category, items_in_stock):
        self.seller_name = seller_name
        self.category = category
        self.items_in_stock = items_in_stock

    def add_seller(self):
        self



class Items(Seller):

    def __init__(self, seller_name, category, items_in_stock, item_name, price):
        super().__init__(seller_name, category, items_in_stock)
        self.item_name = item_name
        self.price = price

    def add_item(item_name, price):
