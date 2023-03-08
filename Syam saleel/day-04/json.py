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
    f = open("G:\\2023-bm-batch-01\\Syam saleel\\day-04\\new.json", "w")
    json.dump(sample_dict, f)
except Exception as e:
    print("Error ", e)

# Read the JSON file
""" json.dump() function is used to write the dictionary to disk, and 
the json.load() function is used to read the contents of the file into a Python dictionary."""
try:
    f = open("day4.txt", "r")
    dict_2= json.load(f)
    f.close()
except Exception as e:
    print("Error reading JSON file:", e)

dict_2["remarks"] = "Modified"

try:
    f = open("day4.txt", "w")
    json.dump(dict_2, f)
    f.close()
except Exception as e:
    print("Error writing JSON file:", e)