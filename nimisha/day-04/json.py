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
try:
    f =open("F:\\zlight-training\\2023-bm-batch-01\\nimisha\\day-04\\json","w")
    json.dumps(sample_dict, f)
except:
    print("something is wrong")

# to read this json file

f= open("F:\\zlight-training\\2023-bm-batch-01\\nimisha\\day-04\\json","r")
dict= json.loads(f)
dict["remarks"]="Modified"

f.close()



