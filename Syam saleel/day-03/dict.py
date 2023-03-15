
"""VI. Consider below Dictionary"""
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

def  searc_dict(key):
    if key in current_dictionary.keys():
        return current_dictionary[key]
    else:
        for data in current_dictionary:
            if isinstance(current_dictionary[data],dict):
                if key in current_dictionary[data].keys():
                    return current_dictionary[data][key]
            elif isinstance(current_dictionary[data], list):
                for value in current_dictionary[data]:
                    if isinstance (value, dict):
                         if key in value.keys():
                            if data == "services":
                                return value[key]
                            else:
                                return "key not found"
                        
    return "key not found"


print(searc_dict("service_status"))   
"""               
find_key = input("enter a key you want :")
print(searc_dict(find_key))"""

#2
"""
key = input("enter the key:-")
value = current_dictionary.get(key)
if value:
    print(value)
else:
    print("Key is not at all present in the dictionary")
"""