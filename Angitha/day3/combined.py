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
dict1 = []
# for item in data:
    # dict1.append(dict(zip(fields,item)))
# print(dict1)


dict2 = {}
for item in data:
    wo_id = dict(zip(fields, item))["wo_id"]
    wo_date = dict(zip(fields, item))["work_order_date"]
    wo_details = dict(zip(fields, item))["work_order_details"]
    dict2[wo_id] = {
        "work_order_details": wo_details,
        "wo_date": wo_date
    }
print(dict2)


    
# dict1 = []
# for item in data:
#     dict1.append(dict(zip(fields,item)))
# print(dict1)
