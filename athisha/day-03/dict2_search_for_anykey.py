"""VI. Consider below Dictionary

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
If Key is not present within the dictionary, it should display as "Key is not at all present in the dictionary"""





"""2. Traverse in the Dictionary to search for any Key, it should return the corresponding value without any errors.
If Key is not present within the dictionary, it should display as "Key is not at all present in the dictionary"""

current_dictionary = {'product_id': '0x24e78',
                      'product_label': 'strawberry',
                      'fulfillment': {'fulfillment_id': '0x24e73',
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
                                              'service_division_criteria':'business_id',
                                              'service_status': 'Ready',
                                              'service_function': 'packaging system'
                                          }
                                      ]}}
#key is parameter
def search_dictionary(key):
    results = []# stored matching value
    if key in current_dictionary.keys():
        return current_dictionary[key]
    else:
        for data in current_dictionary.values():
            if isinstance(data, dict):
                if key in data:
                    results.append(data[key])
                elif 'services' in data:
                    for service in data['services']:
                        if key in service:
                            results.append(service[key])
        if len(results) == 0:
            return "The key is not present within the dictionary."
        else:
            return results


key = input("Enter a key to search for: ")
results = search_dictionary(key)
print(results)

# current_dictionary = {'product_id': '0x24e78',
#                       'product_label': 'strawberry',
#                       'fulfillment': {'fulfillment_id': '0x24e73',
#                                       'group_name': 'General',
#                                       'services': [
#                                           {
#                                               'service_id': '0x24e70',
#                                               'service_name': 'shipment',
#                                               'service_division_criteria': 'business_id',
#                                                             'service_status': 'Packing Completion Pending',
#                                                             'service_function': 'Shipment system'
#                                           },
#                                           {
#                                               'service_id': '0x24e72',
#                                               'service_name': 'package',
#                                               'service_division_criteria':
#                                               'business_id',
#                                                             'service_status': 'Ready',
#                                                             'service_function': 'packaging system'
#                                           }
#                                       ]}}


# def search_dictionary(key):  # fun
#     if key in current_dictionary.keys():
#         return current_dictionary[key]
#     else:
#         for data in current_dictionary:
#             # isinstance() using values checking in dict
#             if isinstance(current_dictionary[data], dict):
#                 if key in current_dictionary[data].keys():
#                     return current_dictionary[data][key]
#                 elif 'services' in current_dictionary[data].keys():
#                     for service in current_dictionary[data]['services']:
#                         if key in service.keys():
#                             return service[key]
#         return "The key is not present within the dictionary."  # indicating a key


# # Prompt the user to enter a key to search for
# key = input("Enter a key to search for: ")

# # Search for the key in the dictionary and print the result
# result = search_dictionary(key)
# print(result)
