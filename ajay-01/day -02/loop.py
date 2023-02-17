 #Use FOR and WHILE loop to display the below manner.
#Even Numbers : 10, 8, 6,4,2
#odd Numbers : 9,7,6,5,3,

# Initialize the empyty list.
numbers = [1,2,3,4,5,6,7,8,9,10]
# Display even numbers
print("Even numbers: ", end="")
for num in numbers:
    if num % 2 == 0:
        print(num, end=", ")

# Display odd numbers
print("\nOdd numbers: ", end="")
for num in numbers:
    if num % 2 != 0:
        print(num, end=", ")







