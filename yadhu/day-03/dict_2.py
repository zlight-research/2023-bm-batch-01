dict=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name": "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]
sort_les=[]
sort_gre=[]
print("*******************")
2.1
new_dict={'id':4,'name':"Mr arjun krishna"}
print("new_dict=",new_dict)
2.2
#to get the value of age
dict.sort(key = lambda x:x['age'])
for data in dict:
    #checking the condition
    if data.get('age')<=20:
        #append it into a list
        sort_les.append(data)
    else:
        sort_gre.append(data)
print("age lessthan 20=",sort_les)
print("age greater than 20=",sort_gre)