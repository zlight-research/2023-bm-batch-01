
# JSON file
import json
f = open ('mydict.json', "r")
  
data = json.loads(f.read())
#updated with new attribute
data.update({"remarks" : "Modified"})
file = open("mydict.json", "w")
file.write(json.dumps(data))
f.close()