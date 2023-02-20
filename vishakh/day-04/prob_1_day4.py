
'''
1. Create a txt file day4.txt

1.1 write "This is day4" to day4.txt
1.2 Read the same file, replace  "day4" with "4th day", save it on the same file
1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file

Output sample:

This is 4th day
This is done by : Yadhu

1.4 Read day4.txt save tha in day4.txt to sting.txt file in custom folder (ex: "C:\Temp\sting.txt")

'''
#import package shutil

import shutil

#create and write day4.txt file
day4_file=open(r"F:\File_handle\day4.txt","w")
day4_file.write("This is day4")

#read file day4.txt

day4_file=open(r"F:\File_handle\day4.txt",'r')
read=day4_file.read()
print(read)


#rewrite file day4.txt

day4_file=open(r"F:\File_handle\day4.txt",'w')
day4_file.write("this is 4th day")

#read file day4.txt

day4_file=open(r"F:\File_handle\day4.txt",'r')
read=day4_file.read()
print(read)


#add new value into  file day4.txt
day4_file=open(r"F:\File_handle\day4.txt",'a')
day4_file.write("\nThis is done by:vishakh")

#read the file day4.txt
day4_file=open(r"F:\File_handle\day4.txt",'r')
read=day4_file.read()
print(read)


#copy day4.txt file and save to another location
ssource_path=r"F:\File_handle\day4.txt"
destina_path=r"F:\temp\string.txt"
day4_strfile=shutil.copy(ssource_path,destina_path)

#read the copied file string.txt

day4_strfile1=open(r"F:\temp\string.txt",'r')
day4_strfile1.read()
print(read)

day4_file.close()

