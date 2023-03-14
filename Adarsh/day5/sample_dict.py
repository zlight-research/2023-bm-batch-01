# sample_dict = { "Name":"Syam", "Age":20 }



# 	1. How to read a Dictionary and write into disk as a JSON format?
# 	"C:\Temp\Employee.json"
# 	dict = json.loads("Employee.JSON")

import json #imported json

sample_dict = { "Name":"Syam", "Age":20 }
file = open("employee.json","w") #json file created
file.write(json.dumps(sample_dict)) #dictionary is write into json file
file.close #file closed

# 2. Read the JSON file, add one more attribute "remarks" : "Modified"

file =  open("employee.json","r") #opened json file
data = json.loads(file.read())
data.update({"remarks":"Modified"})#updated attributes to dictionary
file.close #file closed

# 3. Please Re-write to disk.
# {"Name":"Syam", "Age":20, "remarks": "Modified"}

file = open("employee.json", "w")
file.write(json.dumps(data))#writed modified dictionary to json file
file.close #file closed

