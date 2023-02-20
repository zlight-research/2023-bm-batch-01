"""2. Use FOR and WHILE loop to display the below manner.
Even Numbers : 10, 8, 6,4,2
Odd Numbers : 9,7,6,5,3,1

"""
#while loop

start = 10
end = 0

even=[]
odd=[]

num1 = start

while num1 >= end:
    if (num1%2==0):
        even.append(num1)        
    else:
        odd.append(num1)         

    num1 -= 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)



#For loop
num_list = list(range(1, 10)) 
 
odd_nums = [] 
even_nums = [] 
 
for x in num_list:     
    if x % 2 == 0:         
        even_nums.append(x) 
    else:        
        odd_nums.append(x) 
 
print("even numbers:",even_nums) 
#[2, 4, 6, 8] 
print("odd numbera:",odd_nums) 
#[1, 3, 5, 7, 9] 