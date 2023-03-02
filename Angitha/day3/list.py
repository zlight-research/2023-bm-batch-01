OLD = ['name', 'age', 'gender']
NEW = ['%({})s'.format(item) for item in OLD]
print(f"NEW: {NEW}")