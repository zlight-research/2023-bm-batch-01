"""2. Use FOR and WHILE loop to display the below manner.

Even Numbers : 10, 8, 6,4,2

Odd Numbers : 9,7,6,5,3,1
"""
#While loop


starting = 1
ending = 10

# empty list even and odd

evenNum= []
oddNum = []

while ending >= starting:  # while loop checking condition
    if ending % 2 == 0:
   
        evenNum.append(ending)
    else:

        oddNum.append(ending)

    ending = ending-1


print("even numbers:", evenNum)
print("odd numbers:", oddNum)

#For loop



start = 10
end = 0

#empty list created

even=[]
odd=[]


for num1 in range(start, end, -1):  #checking for loop condition
    if (num1%2==0):
        even.append(num1)        
    else:
        odd.append(num1)         


print("Even:",even)
print("Odd:",odd) 