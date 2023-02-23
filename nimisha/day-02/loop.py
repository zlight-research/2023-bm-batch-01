'''Use FOR and WHILE loop to display the below manner.
Even Numbers : 10, 8, 6,4,2
Odd Numbers : 9,7,6,5,3,1'''

# using for loop
# list=[10,9,8,7,6,5,4,3,2,1]
# even=[]
# odd=[]
# for i in list :
#   if(i % 2 ==0):
#     even.append(i)
#   else:
#     odd.append(i)
#     print(" even no:",even)
#     print("odd no:",odd)

    # using While loop


list1=[1,2,3,4,5,6,7,8,9,10]
num=0
even=[]
odd=[]
while(num<len(list1)):
      if list1[num]% 2==0 :
         even.append(list1[num])
      else:
         odd.append(list1[num])
        #  num += 1
         print("even no:",even)
         print("odd no:",odd)