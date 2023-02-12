#1.1
#list of dictionary
dict=[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
# code to sort list on date
dict.sort(key = lambda x:x['age'])
#print result
print ("result", str(dict))
print("*****************")
#1.2
update=dict[2]
#to update the name syam to shobhana
update.update({'name':'Shobhana'})
print(dict)
#1.3
#to iterate the dictionary
for data in dict:
    #get() to return the value of the given key
    name=data.get('name')
    #checking condition
    if name=="Ajay":
        data.update({'Gender ':'Male'})
print(dict)