"""Please sort the dictionary based on Age"""

school=[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
print("sorting by age:")
"""firstly we sort only the age in ascendeing order"""
print(sorted(school,key=lambda i:i['age']))
"""then we sort """
"""lambda we use supplying a fn as a key parameter to sorted"""




"""Change the Name of id = 3 from syam to Shobhana"""

school=[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]

school[2]["name"]="shobana"
"""In this we can rename the yadhu to shobana"""
"""[0] is the index of list"""
print(school)

"""Update Gender "Male" only for "Ajay" record"""
school=[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
school[1]["Gender"]="Male"
"""In this we can add Gender :male only for Ajay index[1]"""
print(school)






