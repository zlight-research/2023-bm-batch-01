""" Use FOR and WHILE loop to display the below manner."""
"""EVEN NUMBER and  ODD NUMBER"""
n= 10
even=[]
odd=[]
while n>0:
    if(n%2==0):
        even.append(n)
        """even num"""
    else:
        odd.append(n)
        """odd num"""
    n=n-1
val=','.join(map(str,even))
print("Even number:",val)
val=','.join(map(str,odd))
print("Odd number:",val)



    

