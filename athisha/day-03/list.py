"""consider below list

OLD = ['name', 'age', 'gender']

Construct new list from above list "OLD"
NEW :  ['%(name)s', '%(age)s', '%(gender)s']"""

# item as the value you are putting into the list

OLD = ['name', 'age', 'gender']
new = ['%%(%s)s' % item for item in OLD] #concatenating string  using
print("New  : ", new)  # printing the final string list
