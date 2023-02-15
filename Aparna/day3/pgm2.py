# 1. create a new dictionary with {id: <>, "name":<"Mr. / Mrs. f_name, l_name">}
# 2. Please construct below format

# {" Age <= 20": [{<f_name,l_name>},{<f_name,l_name>}],
# " Age > 20": [{<f_name,l_name>},{<f_name,l_name>}],
# }

dict=[{"id":1, "f_name":"yadhu", "l_name":"kumar","gender":"M","age":25},
      {"id":2, "f_name":"Ajay","l_name":"Gopi","gender":"M","age":16},
      {"id":3, "f_name":"syam","l_name":"warrier","gender":"F","age":22}]
# created an empty list
new_data=[]
# used for-loop with if condition and append the resultwith new string
for sep in dict:
    if sep["gender"]=="M":
        name="Mr." + sep["l_name"]+","+sep["f_name"]
    else:
        name="Mrs."+sep["l_name"]+","+sep["f_name"]
    new_data.append({"id":sep["id"],"name":name,"age":sep["age"]})
print(new_data)
above=[]
below=[]
for i in new_data:
    if i["age"]<=20:
        lat={"age":i["age"],"name":i["name"]}
        above.append({"name":i["name"]})
    else:
        lat={"age":i["age"],"name":i["name"]}
        below.append({"name":i["name"]})
nw={"age<=28":above,"age>20":below}
print(nw)
