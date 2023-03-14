"""
III. Created two lists and combined both to create a dict as asked.
fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]

1. create below dict as given below.
[{"wo_id": <WO-01>, "work_order_date":<>,"work_order_details":<>},
{"wo_id": <WO-02> ,"work_order_date":<>,"work_order_details":<>},
{"wo_id": <WO-03>, "work_order_date":<>,"work_order_details":<>}]

2. create a dict as given below format
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

#create a list and list of set


fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]




#some empty list can create

work_ord_id,wo_date,wo_detailes=[],[],[]

#checking the item in data true then append to the empty lists

for values in data:
    for item in values:
        if "WO" in item:
            work_ord_id.append(item)
            
        elif "2022" in item:
            wo_date.append(item)
        else:
            wo_detailes.append(item)

#new empty lists create

fields_data_join1=[]

#join  fields and data append to craete a list of dictionary

fields_data_join1.append({fields[0]:work_ord_id[0],fields[1]:wo_date[0],fields[2]:wo_detailes[0]})
fields_data_join1.append({fields[0]:work_ord_id[1],fields[1]:wo_date[1],fields[2]:wo_detailes[1]})  
fields_data_join1.append({fields[0]:work_ord_id[2],fields[1]:wo_date[2],fields[2]:wo_detailes[2]}) 

#q1
#display the output

print(fields_data_join1)




#new list create

fields_data_join2=[]




#join the the fields and data and append the lis of another format


fields_data_join2.append({work_ord_id[0]:{fields[2]:wo_detailes[0],fields[1]:wo_date[0]}})
fields_data_join2.append({work_ord_id[1]:{fields[2]:wo_detailes[1],fields[1]:wo_date[1]}})  
fields_data_join2.append({work_ord_id[2]:{fields[2]:wo_detailes[2],fields[1]:wo_date[2]}}) 

#display_output

print(fields_data_join2)



