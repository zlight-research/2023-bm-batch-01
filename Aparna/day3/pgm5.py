# V. consider below list
# OLD = ['name', 'age', 'gender']

# # Construct new list from above list "OLD"
# # NEW :  ['%(name)s', '%(age)s', '%(gender)s']

old=[]
# to input the datas
name=input("enter name:")
old.append(name)
age=int(input("enter age:"))
old.append(age)
gender=input("enter gender:")
old.append(gender)
new=[f'%({old[0]})s',f'%({old[1]})s',f'%({old[2]})s']
print("old=",old)
print('\"new=',new)