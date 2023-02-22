

'''
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

 
1. If I need to get all the service_ids in a list ['0x24e70', '0x24e72']
2. Traverse in the Dictionary to search for any Key, it should return the corresponding value without any errors.
If Key is not present within the dictionary, it should display as "Key is not at all present in the dictionary'''

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

def search_dictionary(key):
    
    if key in current_dictionary.keys():
        return current_dictionary[key]
    else:
        for i in current_dictionary:
            if isinstance(current_dictionary[i], dict):
                if key in current_dictionary[i].keys():
                    return current_dictionary[i][key]
            elif isinstance(current_dictionary[i], list):
                for value in current_dictionary[i]:
                    if isinstance (value, dict):
                        if key in current_dictionary[value].keys():
                            return value[key]
            else:
                print("key is not present in the dicitonary")
                        
new_key = input("enter a key you want :")
print(search_dictionary(new_key))