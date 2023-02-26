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

s=[service['service_id']
        for service in current_dictionary['fulfillment']['services']]
print(s)