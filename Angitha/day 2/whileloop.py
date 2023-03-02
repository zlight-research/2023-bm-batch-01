""" Use FOR and WHILE loop to display the below manner."""
"""EVEN NUMBER"""


# num=[]
even=[]
odd=[]
n= 10
while n>0:
    if(n%2==0):
        even.append(n)
    else:
        odd.append(n)
    n=n-1
val=','.join(map(str,even))

print("Even number:",val)
val=','.join(map(str,odd))

print("Odd number:",val)


