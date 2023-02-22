"""III. Created two lists and combined both to create a dict as asked.
fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]

1. create below dict as given below.
[{"wo_id": <WO-01> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-02> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-03> "work_order_date":<>"work_order_details":<>}]

2. create a dict as given below format
[{"WO-01": {
"work_order_details" : <"work_order_details">,
"wo_date": <>
},
{"WO-02": {
"work_order_details" : <"work_order_details">,
"wo_date": <>
}
}]"""

"""1. create below dict as given below.
[{"wo_id": < WO-01 > "work_order_date": <> "work_order_details": <>},
 {"wo_id": < WO-02 > "work_order_date": <> "work_order_details": <> },
 {"wo_id": < WO-03 > "work_order_date": <> "work_order_details": <> }]"""
#Two lists , fields and data

fields = ["wo_id", "work_order_date", "work_order_details"]
data = [{"wo_id": "WO-01", "work_order_date": "2022-05-06", "work_order_details": "Identify what needs to be done to resolve a maintenance issue."},    {"wo_id": "WO-02", "work_order_date": "2022-05-07",
         "work_order_details": "Complete a work order request form to authorize maintenance tasks."},    {"wo_id": "WO-03", "work_order_date": "2022-05-08", "work_order_details": "Maintenance management decides if there is a legitimate need."}]

# file using reader data
# result_dict new dictionary
result_dict = {row["wo_id"]: row for row in data}

print(result_dict)

