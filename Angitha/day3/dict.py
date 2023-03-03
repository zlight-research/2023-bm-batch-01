"""create below dict as given below.
[{"wo_id": <WO-01> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-02> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-03> "work_order_date":<>"work_order_details":<>}]
"""
import re
"""library"""
fields = ["wo_id","work_order_date","work_order_details"]
data = [
    {"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
    {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
    {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}
]
final_list = []
for record in data:
    data_list = list(record)
    for item in record:
        if re.compile("WO-\d*").match(item):
            data_list[0] = item
        elif re.compile("\d*-\d*-\d*").match(item):
            data_list[1] = item
        else:
            data_list[2] = item
    final_list.append(dict(zip(fields, data_list)))
print(final_list)