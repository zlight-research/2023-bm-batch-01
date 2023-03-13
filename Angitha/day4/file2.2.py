import json
sample_dict = '{ "Name":"Syam", "Age":20 }'
data=json.loads(sample_dict)
newdata={"remarks" : "Modified"}
data.update(newdata)
"""update"""
print(data)
