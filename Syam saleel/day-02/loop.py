"""2. Use FOR and WHILE loop to display the below manner.
Even Numbers : 10, 8, 6,4,2
Odd Numbers : 9,7,6,5,3,1
"""

number=int(input("enter a number:"))
while number !=0:
    if number % 2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


#For loop

for i in range(0, 10):
    if i%2==0:
         print(f"{i} is even")
    else:
        print(f"{i}is odd")