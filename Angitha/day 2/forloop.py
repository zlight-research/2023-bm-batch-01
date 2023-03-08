"""Use FOR and WHILE loop to display the below manner."""

"""
Even Numbers : 10, 8, 6,4,2

Odd Numbers : 9,7,6,5,3,1
"""

num= 10,9,8,7,6,5,4,3,2,1
even=[]
odd=[]
for n in num:
    if(n%2==0):
        even.append(n)
        # print("Even Numbers:")
       
    else:

        odd.append(n)
        
        # print("Odd Numbers:")
val=','.join(map(str,even))
print("Even Numbers:",val) 
val=','.join(map(str,odd))
print("Odd Numbers:",val) 






























# even=" "
# odd=" "
# for i in range(1,11):
#   if i %2 ==0:
#        even+= str(i)+","
#   else:
#       odd+= str(i)+ ","
# print("even" + even[:-2])

       
        
        
       
    
       
        
   
