""" create a dict as given below format
[{"WO-01": {
"work_order_details" : <"work_order_details">,
"wo_date": <>
},
{"WO-02": {
"work_order_details" : <"work_order_details">,
"wo_date": <>
}
}]
"""

fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]
# dict1=[]
for values in data:
    for item in values:
        if "WO" in item:
            print(item) 