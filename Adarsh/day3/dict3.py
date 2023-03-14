# III. Created two lists and combined both to create a dict as asked.
import re
fields = ["wo_id", "work_order_date", "work_order_details"]
data = [{"WO-01", "2022-05-06", "Identify what needs to be done to resolve a maintenance issue."},
        {"WO-02", "2022-05-07",
            "Complete a work order request form to authorize maintenance tasks."},
        {"WO-03", "2022-05-08", "Maintenance management decides if there is a legitimate need."}]

# 1. create below dict as given below.
# [{"wo_id": <WO-01>, "work_order_date":<>,"work_order_details":<>},
# {"wo_id": <WO-02> ,"work_order_date":<>,"work_order_details":<>},
# {"wo_id": <WO-03>, "work_order_date":<>,"work_order_details":<>}]

list1 = [] # declared empty list
for element in data:
    list2 = list(element)
    for item in element:
        if re.compile("WO-\d*").match(item):#checks the work id for matches using reg exprn
            list2[0] = item # if true work id stores in list2
        elif re.compile("\d*-\d*-\d*").match(item):#checks the work_order_date for matches using reg exprn
            list2[1] = item # if true work_order_date stores in list2
        else:
            list2[2] = item
    list1.append(dict(zip(fields, list2)))#combines and appends the list elements
print(list1)

# 2. create a dict as given below format
# [{"WO-01": {"work_order_details" : <"work_order_details">,"wo_date": <> },
# {"WO-02": {"work_order_details" : <"work_order_details">,"wo_date": <>}}]

# list3 = []
# for element in data:
#     list4 = list(element)
#     for item in element:
