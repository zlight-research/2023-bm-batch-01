"""consider below list

OLD = ['name', 'age', 'gender']

Construct new list from above list "OLD"
NEW :  ['%(name)s', '%(age)s', '%(gender)s']
"""

OLD = ['name', 'age', 'gender']
NEW = ['%({})s'.format(item) for item in OLD]
"""OLD TO NEW"""
print(f"NEW: {NEW}")