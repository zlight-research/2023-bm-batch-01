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

# print(complex_data)
# print("*"*100)
# sorted_dic=sorted(complex_data,key=lambda d: d['age'])
# print(sorted_dic)


for count,data in enumerate(complex_data):
    # print(count,data)
    if count+1 == len(complex_data):
        break    
    if data['age'] >complex_data[count+1]['age']:
        print("pass")

    

    



