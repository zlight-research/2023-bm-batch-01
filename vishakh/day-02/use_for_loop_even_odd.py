'''
2. Use FOR and WHILE loop to display the below manner.

 

Even Numbers : 10, 8, 6,4,2

Odd Numbers : 9,7,6,5,3,1

'''
#Using for loop to find odd numbers and even numbers in a range

#in a range lower limit and upper limit value stored in to variables

lower_limit=10
upper_limit=0

#empty list created

even_numbers1=[]
odd_numbers1=[]

#checking the number even or odd using for loop and if condition

for num1 in range(lower_limit,upper_limit,-1):
    if (num1%2==0):
        even_numbers1.append(num1)        #empty variable to storing the out put even values
    else:
        odd_numbers1.append(num1)         #empty variable to storing the out put odd values

#display even numbers and odd numbers in a range using for loop        

print("Even numbers using for loop:",even_numbers1)
print("Odd numbers using for loop :",odd_numbers1) 


print("*"*100)


#Using while loop to find odd numbers and even numbers in a range

#in a range lower limit and upper limit value stored in to variables

start=1
end=10

#empty list created

even_numbers2=[]
odd_numbers2=[]

#checking the number even or odd using while loop and if condition

while end>=start:
    if end%2==0:
        even_numbers2.append(end)      #empty variable to storing the out put even values
    else:
    
        odd_numbers2.append(end)        #empty variable to storing the out put odd values

    end=end-1 

#display even numbers and odd numbers in a range using while loop       

print("even numbers using while loop:",even_numbers2)
print("odd numbers using while loop:",odd_numbers2)








        
