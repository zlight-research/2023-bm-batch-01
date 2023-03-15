fields = ["wo_id", "work_order_date", "work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},   
             {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},   
                       {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]
result = []
for d in data:
    wo_id = list(d)[0]
    result.append({wo_id: {
        "work_order_date": list(d)[1],
        "work_order_details": list(d)[2]
    }})
print(result)
