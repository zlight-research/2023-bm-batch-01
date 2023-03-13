"""2. sample_dict = { "Name":"Syam", "Age":20 }
	1. How to read a Dictionary and write into disk as a JSON format?
	"C:\Temp\Employee.json"
	dict = json.loads("Employee.JSON")

	2. Read the JSON file, add one more attribute "remarks" : "Modified"
	3. Please Re-write to disk.

	{"Name":"Syam", "Age":20, "remarks": "Modified"}
"""

import json
sample_dict = { "Name":"Syam", "Age":20 }
sample={}



with open('E:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\dict.json') as f:
    sample = json.loads(f.read())    #read the json file
    print(sample)

#add attribute
sample["remarks"] = "modified"
print(sample)


#rewrite
with open("E:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\dict.json", 'w') as outfile:
	json.dump(sample, outfile)



#read json file
with open('E:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\dict.json') as f:
    sample = json.loads(f.read())    #read the json file
    print(sample)
