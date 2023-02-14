old=[]
name=input("enter name:")
old.append(name)
age=int(input("enter age:"))
old.append(age)
gender=input("enter gender:")
old.append(gender)
new=[f'%({old[0]})s',f'%({old[1]})s',f'%({old[2]})s']
print("old=",old)
print('\"new=',new)