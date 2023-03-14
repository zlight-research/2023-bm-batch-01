

#create a nested dictionary of data

seller_data = {
        "best store": {
            "fresh fruits": [{"item":"apple","price": 50}, {"item":"orange","price":80}, {"item":"banana","price":26}],
            "vegetables": [{"item":"carrot","price":30}, {"item":"onion","price":65}, {"item":"zoya","price":15}]
        },
        "supreme": {
            "cakes": [{"item":"black forest","price":450}, {"item":"white forest","price":520}, {"item":"red velvet","price":860}],
            "drinks": [{"item":"pepsi","price":45}, {"item":"fanta","price":52}, {"item":"latte","price":100}]
        }
    }


#create a class with attributes item_name and item price

class Items:

    def __init__(self,item_name:str,item_price:int) :

        self.item_name=item_name

        self.item_price=item_price

    
    # default method to set the item name and price per unit
    
    def add_items(self,seller_name: str,catagory: str)  :
            for keys,values in seller_data.items():
                if seller_name==keys:
                    for catogorys,catagory_data in values.items():
                        if catogorys ==catagory:
                            catagory_data.append({"item":self.item_name,"price": self.item_price})
                            print(seller_data) 
                            


#create a class Seller with attributes seller_name,catagory,items_in_stock                                 
        
class Seller(Items):

    def __init__(self,seller_name:str=None,category:str=None,items_in_stock:int=None):
              
               
            self.seller_name=seller_name

            self.category=category

            self.items_in_stock=items_in_stock

    #method to create new seller

    def add_seller(self,item_name:str,item_price:int):
        super().__init__(item_name,item_price)
        
        for keys in list(seller_data.items()):
                if self.seller_name!=keys:
          
                      
                    seller_data[self.seller_name]={self.category:[{"item":self.item_name,"item_price":self.item_price}]}
        
        print(seller_data)


    # a function to take the argument and return the cost of the part.


    def price_check(self,item_search:str):
            
        for keys,values in seller_data.items():
            for keys1,values1 in values.items():
                for item in values1:
                    if item_search==item['item']:
                        print("shop name:",keys,"\n",item)
                        
            
    #. a function to return the status if the item is present return the item dictionary else print item is not present

    def item_status(self,item_search):
        list_items=[]
        for keys,values in seller_data.items():
            for keys1,values1 in values.items():
                for item in values1:
                    if item_search==item['item']:
                        list_items.append(item)

        if not list_items:

          print("search item  not  present in seller_data")
        else:


            for item in range(len(list_items)):
               print(list_items[item])
                
                   
         
#enter some values to create a object for adding list items

print("add item in seller shops") 

seller_name1=input("\nenter a seller name: ").lower()         
catagory1=input("enter a catagory: ").lower()          
item_name1=input("enter a item: ").lower()
item_price1=int(input("enter a price: "))
             

# a object create using Item class and the object to call the function add_items()            

obj1=Items(item_name=item_name1,item_price=item_price1)
obj1.add_items(seller_name=seller_name1,catagory=catagory1) 

# enter some values create a objects for adding new seller

print("\nadding new seller with catagory and item")
seller_name2=input("\nenter a seller name:").lower() 
catagory2=input("enter a catagory:").lower()              
item_name2=input("enter a item: ").lower()
item_price2=int(input("enter a price: "))

# a object create using Seller class and the object to call the function add_seller()            

obj2=Seller(seller_name=seller_name2,category=catagory2)
obj2.add_seller(item_name=item_name2,item_price=item_price2)

# enter some values create a objects for searching item to know its price

print("\nitem serach to know it's price  in  seller shops")
item_search3=input("\nenter a item:").lower()

# a object create using Seller class and the object to call the function price_check()            

obj3=Seller().price_check(item_search=item_search3)

#enter a value to create a objects for item status present or not

print("\nsearch a item in a seller shops")
item_search4=input("search for a item:").lower()

# a object create using Seller class and the object to call the function item_status() 
       
obj4=Seller().item_status(item_search=item_search4)


