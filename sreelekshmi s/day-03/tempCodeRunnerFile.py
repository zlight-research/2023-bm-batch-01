<<<<<<< HEAD
import re

fields = ["wo_id","work_order_date","work_order_details"]

data = [    {"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
            {"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
            {"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]
result = [{key: re.sub(r'<|>', '', str(item[key])) for key in fields} for item in data]
print(result)
=======
complexdata=[{"id":1, "name":"Yadhu", "age":25},
{"id":2, "name":"Ajay", "age":16},
{"id":3, "name":"Syam", "age":22}]
update=complexdata[1]
update.update({'gender':'male'})    #update name
print(complexdata)
>>>>>>> ca00cd8fc0f5ab5bcd81daa65f3538febb284735
