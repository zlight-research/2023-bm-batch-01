#two datas created

wo_fields = ["wo_id","work_order_date","work_order_type","work_order_details"]
wo_data = [{"WO-01","2022-05-06","GENERAL","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","EMERGENCY","Complete a work order request form to authorize maintenance tasks."},{
"WO-03","2022-05-08","EMERGENCY","Maintenance management decides if there is a legitimate need."},
{"WO-04","2022-05-09","EMERGENCY","Work orders are assessed by considering the urgency, existing backlog, and team availability."}
]

#empty lists can be created
w_id,w_date,w_type,w_details=[],[],[],[]

#wo_data canbe iterated to find data to seperated append empty specific lists

for values in wo_data:
    for item in values:
        if "WO" in item:
            w_id.append(item)
            
            
        elif "2022" in item:
            w_date.append(item)
        elif "EMER" in item:
            w_type.append(item)
        elif "GENERAL" in item:
            w_type.append(item)

            
        else:
            w_details.append(item)

#empty lists created one for emergency another for general type

out_put_EME=[]
out_put_GENE=[]

# compare wo_fields and wo_data  append some values into empty list for emergency

out_put_EME.append({wo_fields[0]:w_id[1],wo_fields[3]:w_details[1],wo_fields[1]:w_date[1]})
out_put_EME.append({wo_fields[0]:w_id[2],wo_fields[3]:w_details[2],wo_fields[1]:w_date[2]})
out_put_EME.append({wo_fields[0]:w_id[3],wo_fields[3]:w_details[3],wo_fields[1]:w_date[3]})

#compare wo_fields and wo_data  append some values into empty list for general

out_put_GENE.append({wo_fields[0]:w_id[0],wo_fields[3]:w_details[0],wo_fields[1]:w_date[0]})

#join the two dictionaries emergency and general to one dictionaray

final_output={"EMERGENCY":out_put_EME,"GENERAL":out_put_GENE}
#final output_print
print(final_output)





