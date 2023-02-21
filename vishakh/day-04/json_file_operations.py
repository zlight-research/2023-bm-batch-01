'''

2. sample_dict = { "Name":"Syam", "Age":20 }


1. How to read a Dictionary and write into disk as a JSON format?
"C:\Temp\Employee.json"
dict = json.loads("Employee.JSON")

2. Read the JSON file, add one more attribute "remarks" : "Modified"
3. Please Re-write to disk.

{"Name":"Syam", "Age":20, "remarks": "Modified"}




'''
#json package import

import json

#craete a dictionary with value
sample_dict={"Name":"Syam","Age":20}

#empty dictionary create
data={}

#create json file and write it (dictionary converted into json file)
with open(r"F:\\File_handle\\Employee.json",'w') as output:
     json.dump(sample_dict,output)

#read the json file
with open(r"F:\\File_handle\\Employee.json",'r') as input:    
   data=json.load(input)    
print(data)



#add a attribute "remarks":"Modified" 
data['remarks']='Modified'
print(data)


#write into json file updated dictionary to json
with open(r"F:\\File_handle\\Employee.json",'w') as output:
     json.dump(data,output)
#read json file
with open(r"F:\\File_handle\\Employee.json")  as f:
    data1=json.load(f)
print(data1)       

