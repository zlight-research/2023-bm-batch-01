<<<<<<< HEAD
"""V. consider below list
OLD = ['name', 'age', 'gender']

Construct new list from above list "OLD"
NEW :  ['%(name)s', '%(age)s', '%(gender)s']
"""




OLD = ['name', 'age', 'gender']
NEW = ['%({})s'.format(item) for item in OLD]
print(f"NEW: {NEW}")

=======
"""V. consider below list
OLD = ['name', 'age', 'gender']

Construct new list from above list "OLD"
NEW :  ['%(name)s', '%(age)s', '%(gender)s']
"""




OLD = ['name', 'age', 'gender']
NEW = ['%({})s'.format(item) for item in OLD]
print(f"NEW: {NEW}")

>>>>>>> ca00cd8fc0f5ab5bcd81daa65f3538febb284735
