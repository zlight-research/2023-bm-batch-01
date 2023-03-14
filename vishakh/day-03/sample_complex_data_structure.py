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
#create a data employee_dic

employee_dic=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]

#create two empty lists

new_employee_dic1=[]
new_employee_dic2=[]

#iterate datas in list and adding a string to some values in dic

for data in employee_dic:

  if data["gender"]=="M":
    data["f_name"]="Mr."+data["f_name"]
    new_employee_dic1.append(data)
  else:
    data["f_name"]="Mrs."+data["f_name"]
    new_employee_dic2.append(data)

#adding two lists

employee_dic1=new_employee_dic1+new_employee_dic2

#display first format ouput

print(employee_dic1) 

#two empty lists created
age_less_or_eaqual_20=[]
age_great_20=[]

#iterate some values and conditiom check and append the values in to empty lists

for data in employee_dic1:
    if data["age"]<=20:

      age_less_or_eaqual_20.append((data["f_name"],data["l_name"]))

    else:
     
      age_great_20.append((data["f_name"],data["l_name"]))

#display the final result 

result={" Age <= 20":age_less_or_eaqual_20," Age > 20":age_great_20 }
print(result)