'''II. Look at sample complex data structure
[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
2. Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
}'''


# assigining the   values to dictionary
data=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


data1=[]
# evaluating the conditions
for i in data:
    if i["gender"]=='F':
        name='Mrs.'+i['f_name']+' '+i['l_name']
    else:
        name='Mr.'+i['f_name']+' '+i['l_name']
    data1.append({"id":i["id"],"name":name})
# printing the result
print(data1)


'''2. Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
}'''

data=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]

#  evaluating the loop condition
new_data=[]
for i1 in data:
    if i1["age"]<=20 :
        new_data.append({"f_name": i1["f_name"], "l_name": i1["l_name"]})
    else:
        new_data.append({"f_name": i1["f_name"], "l_name": i1["l_name"]})
print(new_data)






