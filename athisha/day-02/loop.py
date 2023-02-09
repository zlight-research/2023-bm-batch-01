"""2. Use FOR and WHILE loop to display the below manner.

Even Numbers : 10, 8, 6,4,2

Odd Numbers : 9,7,6,5,3,1
"""
#While loop

a = int(input("enter starting point:"))  # enter the range of number
n = 1
while n <= a:  # while loop checking condition
    if n % 2 == 0:
        print(n, "is even.")
    else:
        print(n, "is odd.")
    n = n+1

 #    ////////////////////ONE MORE///////////////

starting = 1
ending = 10

# empty list even and odd

evenNum= []
oddNum = []


while ending >= starting:  # while loop checking condition
    if end % 2 == 0:
   
        evenNum.append(end)
    else:

        oddNum.append(end)

    end = end-1


print("even numbers:", evenNum)
print("odd numbers:", oddNum)

#For loop


for i in range(0, 10):

    '''if i % 2 == 0:
        print("Even numbers: ", i)
    else:
        print("Odd numbers:  ", i)'''

    print("{} is even".format(i) if i % 2 == 0 else "{} is odd".format(i))

        #    ////////////////////ONE MORE///////////////


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