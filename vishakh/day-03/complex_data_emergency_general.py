'''
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



'''

#create two datas wo_fields and wo_data

wo_fields = ["wo_id","work_order_date","work_order_type","work_order_details"]
wo_data = [{"WO-01","2022-05-06","GENERAL","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","EMERGENCY","Complete a work order request form to authorize maintenance tasks."},{
"WO-03","2022-05-08","EMERGENCY","Maintenance management decides if there is a legitimate need."},
{"WO-04","2022-05-09","EMERGENCY","Work orders are assessed by considering the urgency, existing backlog, and team availability."}
]

#some empty list are created

w_id,w_date,w_type,w_detail=[],[],[],[]

#some values checking in wo_data values are find then append to empty list
for values in wo_data:
    for item in values:
        if "WO" in item:
            w_id.append(item)
        elif "2022" in item:
            w_date.append(item)
        elif "EM" and "GE" in item:
            w_type.append(item
                          )
        else:
            w_detail.append(item)
  

#new  empty list create 

work_data_join=[]

#comparing two datas and append to empty list

work_data_join.append({wo_fields[0]:w_id[0],wo_fields[1]:w_date[0],wo_fields[3]:w_detail[0]})
work_data_join.append({wo_fields[0]:w_id[1],wo_fields[1]:w_date[1],wo_fields[3]:w_detail[1]})
work_data_join.append({wo_fields[0]:w_id[2],wo_fields[1]:w_date[2],wo_fields[3]:w_detail[2]})
work_data_join.append({wo_fields[0]:w_id[3],wo_fields[1]:w_date[3],wo_fields[3]:w_detail[3]})


#q1.ans
#display first format

emergency_general_data={w_type[1]:[work_data_join[1],work_data_join[2],work_data_join[3]],w_type[0]:[work_data_join[0]]}

print(emergency_general_data)

#q2.ans

#two dictionary create EMERGENCY and GENERAL

emergency_data={w_type[1]:[work_data_join[1],work_data_join[2],work_data_join[3]]}

general_data={w_type[0]:[work_data_join[0]]}

#display two dictionaries

print(emergency_data)

print(general_data)




                
                
              
        
             
            
                   
        

