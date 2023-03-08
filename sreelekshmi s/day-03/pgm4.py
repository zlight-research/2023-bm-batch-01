<<<<<<< HEAD
"""III. Created two lists and combined both to create a dictionary as asked.
fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]

1. create below dict as given below.
[{"wo_id": <WO-01>, "work_order_date":<>,"work_order_details":<>},
{"wo_id": <WO-02> ,"work_order_date":<>,"work_order_details":<>},
{"wo_id": <WO-03>, "work_order_date":<>,"work_order_details":<>}]
"""
import re

fields = ["wo_id","work_order_date","work_order_details"]
data = [
    {"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
    {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
    {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}
]

new_dict = []
for item in data:
    new_item = {}
    for i, field in enumerate(fields):
        if field == "wo_id":
            new_item[field] = item[i]
        elif field == "work_order_date":
            match = re.search(r'\d{4}-\d{2}-\d{2}', item[i])
            if match:
                new_item[field] = match.group()
            else:
                new_item[field] = ""
        elif field == "work_order_details":
            new_item[field] = re.sub(r'\d{4}-\d{2}-\d{2}', '', item[i]).strip()
    new_dict.append(new_item)

print(new_dict)











=======
"""III. Created two lists and combined both to create a dictionary as asked.
fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]

1. create below dict as given below.
[{"wo_id": <WO-01>, "work_order_date":<>,"work_order_details":<>},
{"wo_id": <WO-02> ,"work_order_date":<>,"work_order_details":<>},
{"wo_id": <WO-03>, "work_order_date":<>,"work_order_details":<>}]
"""
import re

fields = ["wo_id","work_order_date","work_order_details"]
data = [
    {"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
    {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
    {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}
]

new_dict = []
for item in data:
    new_item = {}
    for i, field in enumerate(fields):
        if field == "wo_id":
            new_item[field] = item[i]
        elif field == "work_order_date":
            match = re.search(r'\d{4}-\d{2}-\d{2}', item[i])
            if match:
                new_item[field] = match.group()
            else:
                new_item[field] = ""
        elif field == "work_order_details":
            new_item[field] = re.sub(r'\d{4}-\d{2}-\d{2}', '', item[i]).strip()
    new_dict.append(new_item)

print(new_dict)











>>>>>>> ca00cd8fc0f5ab5bcd81daa65f3538febb284735
