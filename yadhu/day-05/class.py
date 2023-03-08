class seller():
    def __init__(self,seller_name,category,items_in_stock):
        self.name=seller_name
        self.category=category
        self.item=items_in_stock
class item(seller):
    
    def __init__(self,seller_name,category,items_in_stock,item_name,price):
                super().__init__(seller_name,category,items_in_stock)
                self.it_na=item_name
                self.prci=price
                
  
    def method(self):
        seller_data1 = {
                            "best store": {
                             "fresh fruits": [{"item":"apple","price": 50}, {"item":"orange","price":80}, {"item":"banana","price":26}],
                             "vegetables": [{"item":"carrot","price":30}, {"item":"onion","price":65}, {"item":"zoya","price":15}]
                            },
                            "supreme": {
                            "cakes": [{"item":"black forest","price":450}, {"item":"white forest","price":520}, {"item":"red velvet","price":860}],
                            "drinks": [{"item":"pepsi","price":45}, {"item":"fanta","price":52}, {"item":"latte","price":100}]
                                }
                            }
        #insert new item
        
        for data in seller_data1:
            if data==seller_name:
                datas=seller_data1.get(data)
                for data in datas:
                    if category==data:
                         val=datas.get(category)
                         res={"item":item_name,"price": price}
                         val.append(res)
        print(seller_data1)
   
    #to search price
        item=input("enter the item to find price:")
        for data in seller_data1:
              store=seller_data1.get(data)
              for i in store:
                    items=store.get(i)
                    for datas in items:
                        #   print(datas)
                        x=datas.get('item')
                        if x==item:
                              print(datas.get('price'))
    # #to find the item present or not
        items=input("enter the item to check availibility:")
        for data in seller_data1:
            store=seller_data1.get(data)
            for data in store:
                 item=store.get(data)
                 for i in item:
                           x=i.get('item')
                           
                           if items in x:
                              print("present.....")


item_name=input("enter item name:")
price=int(input("enter the price:"))
seller_name=input("enter the seller name:")
category=input("enter the category:")
item_in_stock=input("enter the item in stock:")        
obj1=item(seller_name=seller_name,category=category,item_name=item_name,price=price,items_in_stock=item_in_stock)                        
obj1.method()