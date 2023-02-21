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


#input complex data type employee_data

employee_data=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" : "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]

#new empty list can create
#q1.
new_employee_data = list()


#iterate a values in employee data condition check true then append values into empty list 
for values in employee_data:
  if values["gender"]=='M':
    new_employee_data.append({"id":values["id"],"name":"Mr."+values["f_name"]+","+values["l_name"]})
  elif values["gender"]=='F' and values["age"] >=25:
    new_employee_data.append({"id":values["id"],"name":"Mrs."+values["f_name"]+","+values["l_name"]})
  else:
      new_employee_data.append({"id":values["id"],"name":"Mrs."+values["f_name"]+","+values["l_name"]})
print(new_employee_data) #display output

#q2.
#two empty list can create

age_below_20=[]
age_above_20=[]

#iterate values from employee data condition check  condition to append values two empty lists

for item in employee_data:
  
   age_below_20.append({item['f_name']+","+item['l_name']}) if item['age']<=20 else age_above_20.append({item['f_name']+","+item['l_name']})


#new dictionary can create using above two list     

new_format_employee_data={"Age<=20":age_below_20,"Age>20":age_above_20}

print(new_format_employee_data) #display new format output   
      
