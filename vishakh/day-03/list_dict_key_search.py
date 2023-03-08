"""
VI. Consider below Dictionary
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

 
2. Traverse in the Dictionary to search for any Key, it should return the corresponding value without any errors.
If Key is not present within the dictionary, it should display as "Key is not at all present in the dictionary"


"""


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


#enter a key in current dictionary
        
search_key=input("enter a key:").lower()


#checking the key in current dictionary items and print the key value
    
for keys,values in current_dictionary.items():
    if search_key==keys:
       print(values)

    
         
        




#checking the key in fulfillment dictionary items and print the key value

for keys1,values1 in current_dictionary["fulfillment"].items():
    if search_key==keys1:
        print(values1)  
    
               
                  
#checking the key in service item and print the key value
        
if keys1=="services":
    for item in values1:
        for keys2,values2 in item.items():
            if search_key==keys2:
                print(values2)
            

                    