"""1. Create a txt file day4.txt

1.1 write "This is day4" to day4.txt
1.2 Read the same file, replace  "day4" with "4th day", save it on the same file
1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file

Output sample:

This is 4th day
This is done by : Yadhu

1.4 Read day4.txt save tha in day4.txt to sting.txt file in custom folder (ex: "C:\Temp\sting.txt")"""


# Use file to refer to the file object
#"a" - Append - will append to the end of the file

# escape charater is backslash 


with open(r"D:\zlight\2023-bm-batch-01\athisha\day-04\file_append_read.txt", 'a') as fp:
    fp.write("This is 4th day")
    fp.write("\nThis is done by : Athisha")
    print("hi")
