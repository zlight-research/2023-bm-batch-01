import json
sample_dict = { 
    "Name":"Syam", 
    "Age":20 
    }
with open("Employee.json", "w") as outfile:
    """write json file"""
    json.dump(sample_dict, outfile)
