#Use FOR and WHILE loop to display the below manner.
#FOR LOOP
#enter the range of number
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
#empty list to store the even and odd number
even=[]
odd=[]
# iterating each number in list

for num in range(start, end + 1):
 
    # checking condition
    
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
#to find the reverse of list
even.reverse()
odd.reverse()
#convert the list into string 
even_con=','.join(map(str,even))
odd_con=','.join(map(str,odd))
#print even and odd number
print("even_number=",even_con)
print("odd_number=",odd_con)

#WHILE LOOP
#empty list to store the even and odd number
even=[]
odd=[]
#initialize the value of num as 10
num=10
# iterating each number in list

while(num>1):
    #check the condition
    if num%2==0:
        even.append(num)
        num=num-1
    else:
        odd.append(num)
        num=num-1
#convert the list into string
even=','.join(map(str,even))
odd=','.join(map(str,odd))
#print even and odd number
print("even_number=",even_con)
print("odd_number=",odd_con)