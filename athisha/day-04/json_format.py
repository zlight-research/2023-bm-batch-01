"""2. sample_dict = { "Name":"Syam", "Age":20 }


1. How to read a Dictionary and write into disk as a JSON format?
"C:\Temp\Employee.json"
dict = json.loads("Employee.JSON")

2. Read the JSON file, add one more attribute "remarks" : "Modified"
3. Please Re-write to disk.

{"Name":"Syam", "Age":20, "remarks": "Modified"}

Note :  Include Exception handling, proper comments and meaningful variable names"""



"""1. How to read a Dictionary and write into disk as a JSON format?
"C:\Temp\Employee.json"
dict = json.loads("Employee.JSON")"""


import json # moduel inserted

sample_dict = { "Name":"Syam", "Age":20 } 
# open ()file path,with  stmt using automatically close file object
with open(r"D:\zlight\2023-bm-batch-01\athisha\day-04\Employee.json", 'w') as file: # w writing and any exiting content truncated
    # the json file where the output must be stored
    json.dump(sample_dict, file)

