test = [{"id":1, "f_name":"Akshai", "l_name":"Kumar", "gender":"M", "age":25},
        {"id":2, "f_name":"Suresh", "l_name" : "Gopi", "gender":"M", "age":16},
        {"id":3, "f_name":"Manju", "l_name":"Warrier", "gender":"F", "age":22}]
# Create a dictionary and a list
new_dictionary = dict()
updated_list = list()

new_dictionary["age <= 20"] =[] if len(new_dictionary) == 0 else 0
new_dictionary["age > 20"] = [] if "age>20" not in new_dictionary.keys() else 0
# Add data to list and dictionary
for length in range(len(test)):
    updated_list.append({"id":test[length]["id"],"name":"Mr."+test[length]["f_name"]+","+test[length]["l_name"]}) if test[length]["gender"] == "M" else updated_list.append({"id": test[length]["id"], "name": "Mrs." + test[length]["f_name"] + "," + test[length]["l_name"]})
    new_dictionary["age <= 20"].append({test[length]["f_name"]+","+test[length]["l_name"]}) if test[length]["age"] <= 20 else new_dictionary["age > 20"].append({test[length]["f_name"] + "," + test[length]["l_name"]})
# Display data
print("New list : ",updated_list,"\nNew dict : ",new_dictionary)



# sample_dict = [
#                 {"id":1, "name":"Akshai", "age":25},
#                 {"id":2, "name":"Suresh", "age":16},
#                 {"id":3, "name":"Manju", "age":22}
#               ]

# Sorting the dictionary based on age
# greater = list()
# for length in range(len(sample_dict)-1):
#     key = length + 1
#     if sample_dict[length]["age"] > sample_dict[length + 1]["age"]:
#         pass
#     else:
#         temp = sample_dict[length]
# #         sample_dict[length] = sample_dict[length+1]
# #         sample_dict[length + 1] = temp

# new_list = sorted(sample_dict, key=lambda d: d['age'], reverse=True)

# print(new_list)

# """ Update a value in sample dict """

# sample_dict[1]["name"] = "Shobana"
# print(sample_dict[1])

# sample_dict[2]["gender"] = "Male"
# print(sample_dict[2])