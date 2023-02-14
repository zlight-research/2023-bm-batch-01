
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

"""
services = current_dictionary['fulfillment']['services']
service_ids = [service['service_id'] for service in services]
print(service_ids)
"""


#2
key = "product_label"
value = current_dictionary.get(key)
if value:
    print(value)
else:
    print("Key is not at all present in the dictionary")