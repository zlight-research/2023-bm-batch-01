sample_dict = [
                {"id":1, "name":"Akshai", "age":25},
                {"id":2, "name":"Suresh", "age":16},
                {"id":3, "name":"Manju", "age":22}
              ]
new_list = sorted(sample_dict, key=lambda d: d['age'], reverse=True)

print(new_list)

""" Update a value in sample dict """

sample_dict[1]["name"] = "Shobana"
print(sample_dict[1])

sample_dict[2]["gender"] = "Male"
print(sample_dict[2])