"""1. Create a txt file day4.txt

1.1 write "This is day4" to day4.txt
1.2 Read the same file, replace  "day4" with "4th day", save it on the same file
1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file

Output sample:

This is 4th day
This is done by : Yadhu

1.4 Read day4.txt save tha in day4.txt to sting.txt file in custom folder (ex: "C:\Temp\sting.txt")"""
# file day4.txt is created
f=open("F:\\zlight-training\\2023-bm-batch-01\\nimisha\\day-04\\days4.txt","w")
f.write("This is day4")

f.close()

# Read the same file, replace  "day4" with "4th day", save it on the same file
f=open("F:\\zlight-training\\2023-bm-batch-01\\nimisha\\day-04\\days4.txt","r+")
s=f.read()
s=s.replace("day4","4th day\n")
f.write(s)


# 1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file

f=open("F:\\zlight-training\\2023-bm-batch-01\\nimisha\\day-04\\days4.txt","a")

f.write("\n This is done by:nimisha ")
f.close()

# 