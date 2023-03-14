# V. consider below list
# OLD = ['name', 'age', 'gender']

# Construct new list from above list "OLD"
#NEW :  ['%(name)s', '%(age)s', '%(gender)s']

OLD = ['name', 'age', 'gender']
new = ['%%(%s)s' % item for item in OLD]#concatinating string
print("New  : ", new)