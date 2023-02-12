"""2. Use FOR and WHILE loop to display the below manner.
Even Numbers : 10, 8, 6,4,2
Odd Numbers : 9,7,6,5,3,1
"""
#while loop with string
print("Odd Numbers : ", end="")
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


#For loop

for i in range(10,0,-2):
  print(i)