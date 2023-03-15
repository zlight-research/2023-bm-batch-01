
""" III. Created two lists and combined both to create a dict as asked.
fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]"""

#1create below dict as given below.
fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},     
           {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},    
                   {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]
result = []
for d in data:
    result.append(dict(zip(fields, list(d))))
print(result)



#2create a dict as given below format
fields = ["wo_id", "work_order_date", "work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},   
             {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},   
                       {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]
result = []
for d in data:
    wo_id = list(d)[0]
    result.append({wo_id: {
        "wo_date": list(d)[1],
        "work_order_details": list(d)[2]
    }})
print(result)


#3