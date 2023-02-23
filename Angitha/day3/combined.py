"""create below dict as given below.
[{"wo_id": <WO-01> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-02> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-03> "work_order_date":<>"work_order_details":<>}]
"""



fields = ["wo_id", "work_order_date", "work_order_details"]
data = [
    {"WO-01", "2022-05-06", "Identify what needs to be done to resolve a maintenance issue."},
    {"WO-02", "2022-05-07", "Complete a work order request form to authorize maintenance tasks."},
    {"WO-03", "2022-05-08", "Maintenance management decides if there is a legitimate need."}
]

list_of_dict=[{"wo_id","work_order_date","work_order_details"}
              for value,data in zip(fields,data)]

print(list_of_dict)



# x=0
# while x<3:
#     x+=1
#     num=data[0]
#     # print("wo_id")
#     dict1=dict(zip(fields,num))
#     print(dict1)

# ages = [20, 21, 30]
# names = ["Jhon", "Daniel", "Rob"]
# list_of_dicts = [{"age": value, 'name': name}
#                  for value, name in zip(ages, names)]
# print(list_of_dicts)