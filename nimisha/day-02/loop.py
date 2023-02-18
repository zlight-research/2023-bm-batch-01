'''Use FOR and WHILE loop to display the below manner.
Even Numbers : 10, 8, 6,4,2
Odd Numbers : 9,7,6,5,3,1'''


# using while loop
# list of numbers
list1 = [10, 9,8,7, 6, 5, 4,3,2,1]
num = 0
 

while(num < len(list1)):
 
    # checking condition
    if list1[num] % 2 == 0:
        print( "even nmber :",list1[num])

    else:
      list1[num] % 2!=0 
      print( "odd nmber :",list1[num])
      

    # increment num
    num += 1

    # using for loop
 
        
        
