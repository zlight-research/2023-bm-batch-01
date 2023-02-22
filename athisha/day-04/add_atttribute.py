"""2. Read the JSON file, add one more attribute "remarks" : "Modified" """

import json  # json library imported

sample_dict = '{ "Name":"Syam", "Age":20 }'
# python object to be appended
dict = {"remarks": "Modified"}
 
# parsing JSON string:
result = json.loads(sample_dict)
  
# appending the data
result.update(dict)
 
# the result is a JSON string:
print(json.dumps(result))