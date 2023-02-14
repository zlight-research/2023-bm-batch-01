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

import json # json library imported
sample_dict = '{ "Name":"Syam", "Age":20 }'  # json data string
# Decoding or converting JSON format in dictionary using loads()
dict_obj = json.loads(sample_dict)
print("dict  : ", dict_obj)  # get human object details



"""2. Read the JSON file, add one more attribute "remarks" : "Modified" """


sample_dict = '{ "Name":"Syam", "Age":20 }'
# python object to be appended
dict = {"remarks": "Modified"}
 
# parsing JSON string:
result = json.loads(sample_dict)
  
# appending the data
result.update(dict)
 
# the result is a JSON string:
print(json.dumps(result))








#Note:  Include Exception handling, proper comments and meaningful variable names

"""Exceptions: Exceptions are raised when the program is syntactically correct, but the code resulted in an error. 
This error does not stop the execution of the program, however, it changes the normal flow of the program.

example


import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('This message should go to the log file')

try:    
    1/0
except Exception as e:
    logging.exception(e)"""
