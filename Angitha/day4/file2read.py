
import json 
with open('Employee.json','r') as file:
    """json file read"""
    data=json.load(file)
print(data)
