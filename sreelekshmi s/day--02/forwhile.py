#Use FOR and WHILE loop to display the below manner.
#Even Numbers : 10, 8, 6,4,2
#Odd Numbers : 9,7,6,5,3,1
 

#WHILE LOOP

print("Even numbers:")
i=1
while i<10:
    if  i%2==0:
      print(i,',',end=" " )
    i+=1
print('\n')
print("Odd numbers:")
i=1
while i<10:
    if  i%2==1:
      print(i,',',end=" " )
    i+=1    



#FOR LOOP

i=1
end=10
print('Even numbers:',end=' ' )
for i in range(i, end):
    if  i%2==0:
     print(i,',',end=" " )
print('\n')  

i=1
end=10
print('Odd numbers:',end=' ' )
for i in range(i, end): 
    if  i%2==1:
      print(i,',',end=" " )


      







