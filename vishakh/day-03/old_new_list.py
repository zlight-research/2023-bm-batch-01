"""
V. consider below list
OLD = ['name', 'age', 'gender']

Construct new list from above list "OLD"
NEW :  ['%(name)s', '%(age)s', '%(gender)s']


"""
#create a lis old and input values

old=['name','age','gender'] 

#string formating using f_string method

new=[f'%({old[0]})s',f'%({old[1]})s',f'%({old[2]})s']

#display the new list

print('new:',new)

