"""1. Create a txt file day4.txt

1.1 write "This is day4" to day4.txt
1.2 Read the same file, replace  "day4" with "4th day", save it on the same file
1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file

Output sample:

This is 4th day
This is done by : Yadhu

1.4 Read day4.txt save tha in day4.txt to sting.txt file in custom folder (ex: "C:\Temp\sting.txt")"""
# file day4.txt is created
f=open("days4.txt","w")
f.write("This is day4")
f.close()

#Read the same file, replace  "day4" with "4th day", save it on the same file
s=input("this is 4th day")
f=open("days4.txt","r")
f.truncate(0)
f.write(s)
f.close()