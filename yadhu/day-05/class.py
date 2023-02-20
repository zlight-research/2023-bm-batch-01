"""seller class"""
class seller():
    """__init__ is constructor"""
    def __init__(self,seller_name,category,items_in_stock):
        """by using self we can access the attribute and method of class"""
        self.name=seller_name
        self.category=category
        self.item=items_in_stock
        """inherited"""
class item(seller):
    
    def __init__(self,seller_name,category,items_in_stock,item_name,price):
                super().__init__(seller_name,category,items_in_stock)
                self.it_na=item_name
                self.prci=price
  
    def method(self):
          seller_data={self.name:{self.category:[{"item_name":self.it_na,"price":self.prci}]}}
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
                      print("yes...it present")
                else:
                   print("not present")


item_name=input("enter item name:")
price=int(input("enter the price:"))
seller_name=input("enter the seller name:")
category=input("enter the category:")
item_in_stock=input("enter the item in stock:")
obj1=item(seller_name=seller_name,category=category,item_name=item_name,price=price,items_in_stock=item_in_stock)
obj1.method()
