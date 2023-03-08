"""2. Read the JSON file, add one more attribute "remarks" : "Modified" """

import json # Open the JSON 
sample_dict = '{ "Name":"Syam", "Age":20 }'
dict = {"remarks": "Modified"} # object to be appended
result = json.loads(sample_dict) # parsing JSON string
result.update(dict) # appending the data

with open(r"D:\zlight\2023-bm-batch-01\athisha\day-04\sample_dict.json", 'w') as file: # the updated JSON data to the file .
    json.dump(result, file)