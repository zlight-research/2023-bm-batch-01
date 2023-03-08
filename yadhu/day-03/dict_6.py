#6
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
list_id=[]
x=current_dictionary.get('fulfillment')
y=x.get('services')
id_1=y[0]['service_id']
list_id.append(id_1)
id_2=y[1]['service_id']
list_id.append(id_2)
print(" service_ids=",list_id)