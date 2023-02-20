"""
IV.

wo_fields = ["wo_id","work_order_date","work_order_type","work_order_details"]
wo_data = [{"WO-01","2022-05-06","GENERAL","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","EMERGENCY","Complete a work order request form to authorize maintenance tasks."},{
"WO-03","2022-05-08","EMERGENCY","Maintenance management decides if there is a legitimate need."},
{"WO-04","2022-05-09","EMERGENCY","Work orders are assessed by considering the urgency, existing backlog, and team availability."}
]

1. Please construct the below format.

{"EMERGENCY": [{
"wo_id" : <wo_id>,
"work_order_details" : <work_order_details>,
"wo_date": <wo_date>
},
{
"wo_id" : <wo_id>,
"work_order_details" : <work_order_details>,
"wo_date": <wo_date>
}]
},
{"GENERAL": [{
"wo_id" : <wo_id>,
"work_order_details" : <work_order_details>,
"wo_date": <wo_date>
},
{
"wo_id" : <wo_id>,
"work_order_details" : <work_order_details>,
"wo_date": <wo_date>
}]
}
2. Construct to 2 dict for above scenario. one for EMERGENCY and another for GENERAL
"""


wo_fields = ["wo_id","work_order_date","work_order_type","work_order_details"]
wo_data = [{"WO-01","2022-05-06","GENERAL","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","EMERGENCY","Complete a work order request form to authorize maintenance tasks."},{
"WO-03","2022-05-08","EMERGENCY","Maintenance management decides if there is a legitimate need."},
{"WO-04","2022-05-09","EMERGENCY","Work orders are assessed by considering the urgency, existing backlog, and team availability."}
]

#1
main_dict = {"EMERGENCY": [], "GENERAL": []}

for work_order in wo_data:
    P_dict = dict(zip(wo_fields, work_order))
    if P_dict["work_order_type"] == "EMERGENCY":
        main_dict["EMERGENCY"].append({"wo_id": P_dict["wo_id"], 
                                    "work_order_details": P_dict["work_order_details"],
                                    "wo_date": P_dict["work_order_date"]})
    elif P_dict["work_order_type"] == "GENERAL":
        main_dict["GENERAL"].append({"wo_id": P_dict["wo_id"], 
                                  "work_order_details": P_dict["work_order_details"],
                                  "wo_date": P_dict["work_order_date"]})
    
print(main_dict)
