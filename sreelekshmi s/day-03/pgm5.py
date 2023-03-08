"""Consider below Dictionary
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

Traverse in the Dictionary to search for any Key, it should return the corresponding value without any errors.
If Key is not present within the dictionary, it should display as "Key is not at all present in the dictionary"  in python


  1. If I need to get all the service_ids in a list ['0x24e70', '0x24e72']

"""
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

def traverse_dict(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        for k, v in dictionary.items():
            if isinstance(v, dict):
                value = traverse_dict(v, key)
                if value is not None:
                    return value
        return "Key is not at all present in the dictionary"



s=[service['service_id']
        for service in current_dictionary['fulfillment']['services']]
print(s)