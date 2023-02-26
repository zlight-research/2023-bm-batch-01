"""Use FOR and WHILE loop to display the below manner."""

num=10,9,8,7,6,5,4,3,2,1
even=[]
odd=[]
for n in num:
    if(n%2==0):
        even.append(n)
        """even num"""
    else:
        odd.append(n)
        """odd number"""
val=','.join(map(str,even))
print("Even Numbers:",val)
val=','.join(map(str,odd))
print("Odd Numbers:",val)
        
        


        

 

 

    

		
		 
			
		
			
 
    


