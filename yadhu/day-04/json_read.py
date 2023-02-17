  
# JSON file
import json
f = open ('mydict.json', "r")
# Reading from file
data = json.loads(f.read())
  # Iterating through the json
print(data)
  
# Closing file
f.close()