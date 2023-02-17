"""2. create a dict as given below format
[{"WO-01": {
"work_order_details" : <"work_order_details">,
"wo_date": <>
},
{"WO-02": {
"work_order_details" : <"work_order_details">,
"wo_date": <>
}
}]"""
#Two lists , fields and data
fields = ["wo_id", "wo_date", "work_order_details"]
data = [["WO-01", "2022-05-06", "Identify what needs to be done to resolve a maintenance issue."],
        ["WO-02", "2022-05-07", "Complete a work order request form to authorize maintenance tasks."],
        ["WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."]]

result = []# dict order
for item in data:
    d = {} # new dict
    for i in range(len(fields)):
        # it appends to the result
        d[fields[i]] = item[i]
    result.append(
        {item[0]: {"work_order_details": item[2], "wo_date": item[1]}})

print(result)
