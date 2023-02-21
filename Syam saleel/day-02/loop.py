"""2. Use FOR and WHILE loop to display the below manner.
Even Numbers : 10, 8, 6,4,2
Odd Numbers : 9,7,6,5,3,1
"""
#while loop with string
ist1 = [10, 9,8,7, 6, 5, 4,3,2,1]
Sum = 0
while(Sum < len(list)):
    # checking condition
    if list[Sum] % 2 == 0:
        print( "even nmber :",list[Sum])
    else:
      list[Sum] % 2!=0 
      print( "odd nmber :",list[Sum])
      

    # increment Sum
    Sum += 1
"""print("Odd Numbers : ", end="")
i = 9
while i >= 1:
    print(i, end=", ")
    i -= 2
    i -= 1

#while loop with integer
even_numbers = []
i = 10
while i >= 2:
    even_numbers.append(i)
    i -= 2
print((even_numbers))
"""

#For loop

list = [10, 9,8,7, 6, 5, 4,3,2,1]
for Sum in list:
    if Sum % 2 == 0:
        print("even number:", Sum)
    else :
        Sum %2 !=0
        print("odd number:", Sum)
        