#  Please sort the dictionary based on Age

school={'Ajay':16,'syam':22,'yadhu':25}
print(school)

# Change the Name of id = 3 from syam to Shobhana
school={'Ajay':16,'syam':22,'yadhu':25}
school['shobana']=school['yadhu']
del school['yadhu']
print(school)

# Update Gender "Male" only for "Ajay" record.
school={'Ajay':16,'syam':22,'yadhu':25}
school['Gender']='male'
print(school)


school=[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]


print(school)




