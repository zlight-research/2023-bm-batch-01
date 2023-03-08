
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

class items:
    def __init__(self,item_name,item_price):
        self.item_name=item_name
        self.item_price=item_price
  
    def add(self):
       # seller_name = input("Enter seller name: ")
       # category = input("Enter category: ")
       #to add items
        for keys, values in seller_data.items():
            if seller_name == keys:
                for categ, category_data in values.items():
                    if categ == category:
                        category_data.append({"item": self.item_name, "price": self.item_price})
                        print(seller_data)
    def get_price(item_name):
        for seller, categories in seller_data.items():
            for category, items in categories.items():
                for item in items:
                    if item["item"] == item_name:
                        return item
        return None
    def check_item(item_name):
        for seller, categories in seller_data.items():
            for category, items in categories.items():
                for item in items:
                    if item["item"] == item_name:
                        return item
        return None

class seller(items):
    def __init__(self, seller_name,category,item_in_stock):
        self.seller_name=seller_name
        self.category=category
        self.item_in_stock=item_in_stock

seller_name = input("Enter seller name: ")
category = input("Enter category: ")
item_name = input("Enter item name: ")
item_price = int(input("Enter item price: "))
items(item_name, item_price).add()

search_item_name = input("Enter item name to search: ")
item = items.check_item(search_item_name)
if item:
    print(f"Item '{item['item']}' found with price {item['price']}.")
else:
    print(f"Item '{search_item_name}' not found.")
# insert into seller class
#items(item_name="mango",item_price=120).add(seller_name="best store",category="fresh fruits")

#to find the seller item


       

