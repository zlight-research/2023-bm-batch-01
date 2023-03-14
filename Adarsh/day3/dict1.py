# __I) sample complex data structure
dict = [{"id": 1, "name": "Yadhu", "age": 25}, {"id": 2, "name": "Ajay", "age": 16},
        {"id": 3, "name": "Syam", "age": 22}]
print(dict)

# 1.  sort the dictionary based on Age.
print("List sorted by age: ")
print(sorted(dict, key=lambda x: x['age']))#sort operation using lambda

# 2. Change the Name of id = 3 from syam to Shobhana

dict[2].update({'name': 'shobhana'})  #updated the name
print(dict)

# 3. Update Gender "Male" only for "Ajay" record.
dict[1].update(gender='Male')  # added a new key and value
print(dict) # print the result