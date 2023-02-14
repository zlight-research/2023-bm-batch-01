
wo_fields = ["wo_id","work_order_date","work_order_type","work_order_details"]
wo_data = [{"WO-01","2022-05-06","GENERAL","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","EMERGENCY","Complete a work order request form to authorize maintenance tasks."},{
"WO-03","2022-05-08","EMERGENCY","Maintenance management decides if there is a legitimate need."},
{"WO-04","2022-05-09","EMERGENCY","Work orders are assessed by considering the urgency, existing backlog, and team availability."}
]

new=[]
for datas in wo_data:
    merge=zip(wo_fields,datas)
    con_dic=dict(merge)
    new.append(con_dic)

for data in new:
    e={"emergency":[{"wo_id":data["wo_id"],"work_order_date":data["work_order_date"],"work_order_details":data["work_order_details"]}]}
    g={"general":[{"wo_id":data["wo_id"],"work_order_date":data["work_order_date"],"work_order_details":data["work_order_details"]}]}
print(e)
print(g)