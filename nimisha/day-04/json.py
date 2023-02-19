'''2. sample_dict = { "Name":"Syam", "Age":20 }


1. How to read a Dictionary and write into disk as a JSON format?
"C:\Temp\Employee.json"
dict = json.loads("Employee.JSON")

2. Read the JSON file, add one more attribute "remarks" : "Modified"
3. Please Re-write to disk.

{"Name":"Syam", "Age":20, "remarks": "Modified"}'''



# How to read a Dictionary and write into disk as a JSON format?
import json
sample_dict=  { "Name":"Syam", "Age":20 }
dict = json.loads(sample_dict)
