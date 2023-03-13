"""Look at sample complex data structure
[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
{"id":2, "f_name":"Ajay", "l_name" = "Gopi", "gender":"M", "age":16},
{"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
2. Please construct below format

{" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
" Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],}"""

complexdata=[{"id":1, "f_name":"yadhu", "l_name":"Kumar", "gender":"M", "age":25},
             {"id":2, "f_name":"Ajay", "l_name" :"Gopi", "gender":"M", "age":16},
             {"id":3, "f_name":"syam", "l_name":"Warrier", "gender":"F", "age":22}]


new1_dict={" Age <= 20":[]}
new2_dict={" Age > 20":[]}

for item in complexdata:
    full_name={item["f_name"],item["l_name"]}




    if item["age"]<=20:

     new1_dict[" Age <= 20"].append(full_name)

    else:
      new2_dict[" Age > 20"].append(full_name)

print(new1_dict)
print(new2_dict)


