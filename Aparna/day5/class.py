# 1. Create a class for Seller and Items with following attributes and operations
# Seller class has seller name, category,  items_in_stock
# items class has item_name and price.
# 1. Items should have default method to set the item name and price per unit

 

# 2. Seller class should have initialize operation to

# 2.a Set the seller name (a method to create new seller)

# 2.b a method to add part to the list of items

# 2. c a function to take the argument and return the cost of the part.

# 2.d. a function to return the status if the item is present in the seller side, it should not be case-sensitive



# seller_data = {
#         "best store": {
#             "fresh fruits": [{"item":"apple","price": 50}, {"item":"orange","price":80}, {"item":"banana","price":26}],
#             "vegetables": [{"item":"carrot","price":30}, {"item":"onion","price":65}, {"item":"zoya","price":15}]
#         },
#         "supreme": {
#             "cakes": [{"item":"black forest","price":450}, {"item":"white forest","price":520}, {"item":"red velvet","price":860}],
#             "drinks": [{"item":"pepsi","price":45}, {"item":"fanta","price":52}, {"item":"latte","price":100}]
#         }
#     }

# to create seller class
class seller():
    # __init__ is constructor
    def __init__(self,seller_name,category,items_in_stock):
        # by using self we can access the attribute and method of class
        self.name=seller_name
        self.category=category
        self.item=items_in_stock
        # inherited the class
class item(seller):
    
    def __init__(self,seller_name,category,items_in_stock,item_name,price):
                super().__init__(seller_name,category,items_in_stock)
                self.itemname=item_name
                self.prcice=price
  
    def method(self):
          seller_data={self.name:{self.category:[{"item_name":self.itemname,"price":self.prcice}]}}
          print("seller_data=",seller_data)
          #to find the price
          item=input("enter the item name to find the price:")
          seller_name=seller_data.get(self.name)
          category=seller_name.get(self.category)
          for data in category:
                if data['item_name']==item:
                      print("price=",data['price'])
                else:
                      print("the item is not avaiable....")
          #to find the item present in the list or not
          to_find=input("enter the item name to find the item present in the seller side:")
          to_find_convert=to_find.lower()
          seller_name=seller_data.get(self.name)
          category=seller_name.get(self.category)
          for data in category:
                if to_find_convert in data['item_name']:
                      print("present")
                else:
                   print("not present")


item_name=input("enter item name:")
price=int(input("enter the price:"))
seller_name=input("enter the seller name:")
category=input("enter the category:")
item_in_stock=input("enter the item in stock:")
obj1=item(seller_name=seller_name,category=category,item_name=item_name,price=price,items_in_stock=item_in_stock)
obj1.method()
