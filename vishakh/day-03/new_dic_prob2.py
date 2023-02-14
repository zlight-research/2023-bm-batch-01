'''
II. Look at sample complex data structure
[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
2. Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
}



'''

employee_dic=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]

new_employee_dic1=[]
new_employee_dic2=[]
for data in employee_dic:

  if data["gender"]=="M":
    data["f_name"]="Mr."+data["f_name"]
    new_employee_dic1.append(data)
  else:
    data["f_name"]="Mrs."+data["f_name"]
    new_employee_dic2.append(data)
employee_dic1=new_employee_dic1+new_employee_dic2
print("*"*100)
print(employee_dic1) 
print("*"*100)

age_less_or_eaqual_20=[]
age_great_20=[]
for data in employee_dic1:
    if data["age"]<=20:

     age_less_or_eaqual_20.extend((data["f_name","l_name"]))

    else:
     
     age_great_20.extend((data["f_name","l_name"]))

print(age_less_or_eaqual_20)

print("*"*100)

print(age_great_20)