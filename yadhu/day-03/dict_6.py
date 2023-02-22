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

#2
keyy=input("enter the key:")
if keyy=="service_id" or keyy=="service_name" or keyy=="service_division_criteria" or keyy=="service_status" or keyy=="service_function":
    fulfillment=current_dictionary.get('fulfillment')
    services=fulfillment.get('services')
    for data in range(0,2):
        res=services[data][keyy]
        print(keyy,"==",res)
elif keyy=="fulfillment_id" or keyy=="group_name":
    fulfillment=current_dictionary.get('fulfillment')
    result=fulfillment[keyy]
    print(keyy,"==",result)
elif keyy=="product_id" or keyy=="product_label":
    result=current_dictionary[keyy]
    print(keyy,"==",result)
else:
    print("invalid key.................................")
