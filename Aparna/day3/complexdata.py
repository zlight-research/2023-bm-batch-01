# 1.Look at sample complex data structure

# [
# {"id":1, "name":"Yadhu", "age":25},
# {"id":2, "name":"Ajay", "age":16},
# {"id":3, "name":"Syam", "age":22}]


# 1. Please sort the dictionary based on Age.
dict=[{"id":1, "name":"Yadhu", "age":25},
      {"id":2, "name":"Ajay", "age":16},
      {"id":3, "name":"Syam", "age":22}]
print("sort the dictionary based on Age:")
# sorting the age in ascendeing order
print(sorted(dict,key=lambda i:i['age']))

# 2. Change the Name of id = 3 from syam to Shobhana
dict=[
      {"id":1, "name":"Yadhu", "age":25},
      {"id":2, "name":"Ajay", "age":16},
      {"id":3, "name":"Syam", "age":22}]
update=dict[2]
# update the name syam to shobhana
update.update({'name':'Shobhana'})
print(dict)

# 3. Update Gender "Male" only for "Ajay" record.
dict=[
      {"id":1, "name":"Yadhu", "age":25},
      {"id":2, "name":"Ajay", "age":16},
      {"id":3, "name":"Syam", "age":22}]
for item in dict:
    if item['name']=='Ajay':
        item['gender']='Male'
        print(dict)
