'''I. Look at sample complex data structure

[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]


1. Please sort the dictionary based on Age.
2. Change the Name of id = 3 from syam to Shobhana
3. Update Gender "Male" only for "Ajay" record.'''



''' 1. Please sort the dictionary based on Age.'''
# taking values for sorting
dict=[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]

print(dict)
# giving key value as lamda and sorting them 
sort=sorted(dict,key=lambda s: s['age'])
print("\n",sort)


'''2.Change the Name of id = 3 from syam to Shobhana'''
dict=[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
print("dict =\n",dict)
print("id=",dict["id"])
print("name=",dict["name"])

dict.update({"id":"3","name":"shobana"})
print("\nUpdate dictionary=\n",dict)
print("updated id=",dict["id"])
print("updated name=",dict["name"])


'''3. Update Gender "Male" only for "Ajay" record.'''
print("dict =\n",dict)
print("id=",dict["id"])
print("gender=",dict["gender"])

dict.update({"id":"1","gender":"male"})
print("\nUpdate dictionary=\n",dict)
print("updated id=",dict["id"])
print("updated gender=",dict["gender"])
