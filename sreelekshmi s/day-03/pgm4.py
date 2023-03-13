"""III. Created two lists and combined both to create a dictionary as asked.

fields = ["wo_id","work_order_date","work_order_details"]

data = [
         {"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
         {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
         {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}
       ]

1. create below dict as given below.
[{"wo_id": <WO-01>, "work_order_date":<>,"work_order_details":<>},
{"wo_id": <WO-02> ,"work_order_date":<>,"work_order_details":<>},
{"wo_id": <WO-03>, "work_order_date":<>,"work_order_details":<>}]
"""
fields = ["wo_id","work_order_date","work_order_details"]

data = [
         {"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
         {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
         {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}
       ]
new_list = []
for item in data:
   for i in item:
    new_list.append(i)
#print("new_list=",new_list)


#second
fields = ["wo_id","work_order_date","work_order_details"]

new_list= ['2022-05-06', 'Identify what needs to be done to resolve a maintenance issue.', 'WO-01',
           'Complete a work order request form to authorize maintenance tasks.','2022-05-07','WO-02',
           'Maintenance management decides if there is a legitimate need.', 'WO-03', '2022-05-08'
          ]



list1 = new_list[0:3]     # Contains the first three elements
list2 = new_list[3:6]     # Contains elements 4, 5, and 6
list3 = new_list[6:]      # Contains the remaining elements

dict_list = []
dict_list2 = []
dict_list3= []


# Loop through the new_list and create dictionaries
for i in range(0, len(list1), 3):
    dict_list.append({
        "wo_id": list1[i+2],
        "work_order_date": list1[i],
        "work_order_details": list1[i+1]
    })

for i in range(0, len(list2), 3):
    dict_list2.append({
        "wo_id": list2[i+2],
        "work_order_date": list2[i+1],
        "work_order_details": list2[i]
    })

for i in range(0, len(list3), 3):
    dict_list3.append({
        "wo_id": list3[i+1],
        "work_order_date": list3[i+2],
        "work_order_details": list3[i]
    })


final_dict=dict_list +dict_list2+dict_list3
print(final_dict,"\n")








"""
import re
new_dict = []
for item in data:
    new_item = {}
    for i, field in enumerate(fields):
        if field == "wo_id":
            new_item[field] = item[i]
        elif field == "work_order_date":
            match = re.search(r'\d{4}-\d{2}-\d{2}', item[i])
            if match:
                new_item[field] = match.group()
            else:
                new_item[field] = ""
        elif field == "work_order_details":
            new_item[field] = re.sub(r'\d{4}-\d{2}-\d{2}', '', item[i]).strip()
    new_dict.append(new_item)

print(new_dict)




"""





