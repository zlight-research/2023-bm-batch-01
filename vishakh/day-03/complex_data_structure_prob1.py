'''
 I. Look at sample complex data structure

[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]


1. Please sort the dictionary based on Age.
2. Change the Name of id = 3 from syam to Shobhana
3. Update Gender "Male" only for "Ajay" record.


'''

complex_data=[
{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]

#sorted a value in complex data type using lambda function

print(complex_data)
print("*"*100)
sorted_dic=sorted(complex_data,key=lambda d: d['age'])
print("\n",sorted_dic)
print("*"*100)


""" Update a value in sample dict """

complex_data[2]["name"]="shobana"
print("\n",complex_data)

print("*"*148)

complex_data[1]["gender"]="male"
print("\n",complex_data)
       
       
    



