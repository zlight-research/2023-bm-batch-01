"""2. Use FOR and WHILE loop to display the below manner.
Even Numbers : 10, 8, 6,4,2
Odd Numbers : 9,7,6,5,3,1"""

# --------------using for loop-------------

start = int(input("input starting number:"))  # input starting number in start

even = []  # empty list named of odd
odd = []  # empty list named of even
for start in range(start, 0, -1):
    if start % 2 == 0:
        even.append(start)  # append the value to the list even
    else:
        odd.append(start)  # append the value to the list odd

print("Even Numbers:", even)
print("Odd Numbers:", odd)

# ---------------using while loop-------------------

start = int(input("input starting number:"))  # input starting number in start

even = []  # empty list named of odd
odd = []  # empty list named of even
while start >= 0:
    if start % 2 == 0:
        even.append(start)  # append the value to the list even
    else:
        odd.append(start)  # append the value to the list odd
    start = start - 1
print("Even Numbers:", even)
print("Odd Numbers:", odd)
