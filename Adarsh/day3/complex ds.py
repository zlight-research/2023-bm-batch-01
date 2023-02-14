""" 1) Look at sample complex data structure
[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]

1. Please sort the dictionary based on Age.
2. Change the Name of id = 3 from syam to Shobhana
3. Update Gender "Male" only for "Ajay" record."""

1.
# sorted() with lambda

# Initializing list of dictionaries

myDict = [{"id": 1, "name": "Yadhu", "age": 25}, {"id": 2, "name": "Ajay", "age": 16}, 
          {"id": 3, "name": "Syam", "age": 22}]

# using sorted and lambda to print list sorted
# by age

print("The list printed sorting by age: ")
print(sorted(myDict, key=lambda i: i['age']))



# 2. Change the Name of id = 3 from syam to Shobhana

mydict1 = {"id": 3, "name": "Syam", "age": 22}
mydict1['Syam'] = 'Shobhana'  # changing value
print(mydict1)





#3.Update Gender "Male" only for "Ajay" record.

# append using the update() function.

dict1 = {"id": 2, "name": "Ajay", "age": 16}
dict1.update(gender='Male')  # adding a new key-value pair
print(dict1) # print the result



