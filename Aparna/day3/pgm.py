# III. Created two lists and combined both to create a dict as asked.
# fields = ["wo_id","work_order_date","work_order_details"]
# data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
# {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
# {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]

# 1. create below dict as given below.
# [{"wo_id": <WO-01> "work_order_date":<>"work_order_details":<>},
# {"wo_id": <WO-02> "work_order_date":<>"work_order_details":<>},
# {"wo_id": <WO-03> "work_order_date":<>"work_order_details":<>}]

fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},    
        {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
        {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]
# create new dictionary
new_dict=[]
# iterate data
for datas in data:
    new_dict.append(dict(zip(fields,datas)))
print(new_dict)


# 2. create a dict as given below format
# [{"WO-01": {
# "work_order_details" : <"work_order_details">,
# "wo_date": <>
# },
# {"WO-02": {
# "work_order_details" : <"work_order_details">,
# "wo_date": <>
# }
# }]

for datas in new_dict:
    list=[{"wo-01":{
        "work_order_details":datas["work_order_details"],"work_order_date":datas["work_order_date"]}},
        {"wo-02":{
        "work_order_details":datas["work_order_details"],"work_order_date":datas["work_order_date"]}},
        {"wo-03":{
        "work_order_details":datas["work_order_details"],"work_order_date":datas["work_order_date"]}}

        ]
print(list)