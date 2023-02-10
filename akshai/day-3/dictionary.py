# simple dictionary

sample_dict = {"name":"syam",
                "age":21,
                "name":"aiswarya"}
print(sample_dict)


# nested dictionary

sample_dict = {"name":"syam",
                "language":{"backend": "python",
                            "frontend": "html"}}
# print(sample_dict.get("language"))

# dictionary of lists
for data in sample_dict:
    print(sample_dict[data])

sample_dict = {"name":"syam",
                "language":{"backend": "python",
                            "frontend": "html"}}
test_dict = {"place":"thrissur"}
sample_dict.update({"place":"thrissur"})
print(sample_dict)