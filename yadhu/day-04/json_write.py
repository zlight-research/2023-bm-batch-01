# importing json library
import json
# defining the dictionary
records = { 
        "Name":"syam",
        "age":20
        }
# Open file in write mode
file = open("mydict.json", "w")
# write dictionary into file using json.dumps()
file.write(json.dumps(records))
file.close()