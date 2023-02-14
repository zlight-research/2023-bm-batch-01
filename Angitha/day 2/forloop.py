"""Use FOR and WHILE loop to display the below manner."""
"""EVEN NUMBER"""
# for num in range(10,0,-2): 
#     """Here we give for loop and give Range(10,0,-2,) 
#     Here 10 to 0 numbers """
      
#     print(num)

# """ODD NUMBER"""
# for num in range(9,0,-2): 
#     """Here we give for loop and give Range(9,0,-2,) 
#     Here 9 to 0 numbers """
      
#     print(num)  
# num=int(input("enter the number:"))
# for num in range(10,0,-2): 
#     for number in range(9,0,-2):
#         if(number % 2 != 0):
#             print("{0}".format(number))
 

# print("Element in Even List is : ", Even)
# print("Element in Odd List is : ", Odd)

print("Even num:")
for i in range(10,0,-2):
    if(i%2==0):
        print(i)
print(" Odd num:")
for i in range(9,0,-2):
    if(i%2!=0):
        print(i)