"""1. Create a txt file day4.txt

1.1 write "This is day4" to day4.txt
1.2 Read the same file, replace  "day4" with "4th day", save it on the same file
1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file

Output sample:

This is 4th day
This is done by : Yadhu

1.4 Read day4.txt save tha in day4.txt to sting.txt file in custom folder (ex: "C:\Temp\sting.txt")
"""
#1. write "This is day4" to day4.txt

f=open("C:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\day-04.txt","w")
f.write("this is day4")
f.close()


#2. Read the same file, replace  "day4" with "4th day", save it on the same file

with open("C:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\day-04.txt","r")as file:
    data=file.read()                                    #the read data can store in data
    data=data.replace('day4' ,'4th day')                #replace the word day4 to 4th day
with open("C:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\day-04.txt","w")as file:
     file.write(data)


#3.Read the same file, append "This is done by : <Your_name>" , save it on the same file


f=open("C:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\day-04.txt","a")
f.write("\n this is done by :sreelekshmi")


#4.Read day4.txt save tha in day4.txt to sting.txt file in custom folder (ex: "C:\Temp\sting.txt")


import os
old_name="C:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\day-04.txt"
new_name="C:\\zlight\\2023-bm-batch-01-1\\sreelekshmi s\\day-04\\\\sting.txt"
os.rename(old_name,new_name)
os.chdir(path='C:\Task')

