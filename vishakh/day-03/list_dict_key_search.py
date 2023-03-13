

#create a dictionary

current_dictionary = { 'product_id': '0x24e78',
'product_label': 'strawberry',
'fulfillment':
{ 'fulfillment_id': '0x24e73',
'group_name': 'General',                    
'services': [
{
'service_id': '0x24e70',
'service_name': 'shipment',
'service_division_criteria': 'business_id',
'service_status': 'Packing Completion Pending',
'service_function': 'Shipment system'
},
{
'service_id': '0x24e72',
'service_name': 'package',
'service_division_criteria':
'business_id',
'service_status': 'Ready',
'service_function': 'packaging system'
}
]}}

#create a empty list
key_data=[]

#create a function key_find()

def key_find():
    
    #enter key for search

    search_key=input("enter a key for search:")
   
    #checking the key in main dictionary find append to the empty list

    for keys,values in current_dictionary.items():
        if search_key==keys:
           key_data.append(values)
       

       
        #not in main dictionary then search key for values dictionaries find append to the empty list
        
        elif isinstance(values,dict):
            for keys1,values1 in values.items():
                if keys1==search_key:
                   key_data.append(values1)
                
                #not search key  in values dictionry  then search values of list items find append to the empty list       
    
                elif isinstance(values1,list):
                    for item in values1:
                        for keys2,values2 in item.items():
                           if keys2==search_key:
                               key_data.append(values2)

                          
              
    #the key is not in the list print key is not present inthe dictionary

    if not key_data:

        print("Key is not at all present in the dictionary")
    
    #the key is present in the list then print the values of search key
    else:
        for item in range(len(key_data)):
            print(key_data[item])


key_find()    



