import re

text = "Arithematic operators ,Assignment operators, Comparison operators, Logical operators, Identity operators, Membership operators"
data = re.findall("operators", text)
print(data)