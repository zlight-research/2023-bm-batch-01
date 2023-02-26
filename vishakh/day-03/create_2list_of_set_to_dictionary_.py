'''

III. Created two lists and combined both to create a dict as asked.
fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]

1. create below dict as given below.
[{"wo_id": <WO-01> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-02> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-03> "work_order_date":<>"work_order_details":<>}]

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





'''

#create one list and list of set

fields = ["wo_id","work_order_date","work_order_details"]

data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]

#q.1
#empty dictionaries create
w_id,w_date,wo_detail=[],[],[]

#iterate data
for values in data:
   for item in values:
     #condition to check work_id   and append to empty list
     if "WO" in item:

          w_id.append(item)
     #condition to check work_order_date and append to empty list
     elif "2022" in item:
          w_date.append(item)
     #else work_order_detailes append to empty list
     else:
          wo_detail.append(item)

#create another empty list
first_dict_format=[]

#append to empty list dictionary of data
first_dict_format.append({fields[0]:w_id[0],fields[1]:w_date[0],fields[2]:wo_detail[0]})
first_dict_format.append({fields[0]:w_id[1],fields[1]:w_date[1],fields[2]:wo_detail[1]})
first_dict_format.append({fields[0]:w_id[2],fields[1]:w_date[2],fields[2]:wo_detail[2]})


#display first format output
print(first_dict_format)

#q.2

#empty list_create
second_dic_format=[]

#iterate first_format_output

for data in first_dict_format:
#append a dictionary of format data

     second_dic_format.append({data["wo_id"]:{"work_order_detailes":data["work_order_details"],"work_order_date":data["work_order_date"]}})

#display second format output     
print(second_dic_format)         

