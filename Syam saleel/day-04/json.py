"""2. sample_dict = { "Name":"Syam", "Age":20 }
1. How to read a Dictionary and write into disk as a JSON format?
"C:\Temp\Employee.json"
dict = json.loads("Employee.JSON")
2. Read the JSON file, add one more attribute "remarks" : "Modified"
3. Please Re-write to disk.
{"Name":"Syam", "Age":20, "remarks": "Modified"}
Note :  Include Exception handling, proper comments and meaningful variable names"""

import json
sample_dict = { "Name":"Syam", "Age":20 }
try:
    with open("E:\\Employee.json", "w") as f:
        json.dump(sample_dict, f)
except Exception as e:
    print("Error writing JSON file:", e)

# Read the JSON file
""" json.dump() function is used to write the dictionary to disk, and 
the json.load() function is used to read the contents of the file into a Python dictionary."""
