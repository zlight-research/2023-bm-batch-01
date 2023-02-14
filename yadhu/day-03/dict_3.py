#III. Created two lists and combined both to create a dict as asked


fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]  
new_data=[]
data_tup=[]
for datas in data:
    tup=tuple(datas)
    data_tup.append(tup)
    for tu in data_tup:
        pre=zip(fields,tu)
        old=dict(pre)
        new_data.append(old)
print(new_data)

#2
for datas in new_data:
    list=[{"wo-01":{
        "work_order_details":datas["work_order_details"],"work_order_date":datas["work_order_date"]}},
        {"wo-02":{
        "work_order_details":datas["work_order_details"],"work_order_date":datas["work_order_date"]}},
        {"wo-03":{
        "work_order_details":datas["work_order_details"],"work_order_date":datas["work_order_date"]}}

        ]
print(list)