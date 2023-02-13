
""" 1) Look at sample complex data structure
[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
1. Please sort the dictionary based on Age.
2. Change the Name of id = 3 from syam to Shobhana
3. Update Gender "Male" only for "Ajay" record."""


dict=[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]

for count,data in enumerate(dict):
    #ifdata['age']>20:
        #print(data)
    if count+1==len(dict):
        break
    if data['age']>dict[count+1]['age']:
        print("pass")
#2
dict=[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]

update=dict[2]
#to update the name syam to shobhana
update.update({'name':'Shobhana'})
print(dict)

#3
dict=[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]

for item in dict:
    if item['name']=='Ajay':
        item['gender']='Male'
        print(dict)