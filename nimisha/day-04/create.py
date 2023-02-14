''''1. Create a txt file day4.txt

1.1 write "This is day4" to day4.txt
1.2 Read the same file, replace  "day4" with "4th day", save it on the same file
1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file
Output sample:

This is 4th day
This is done by : Yadhu

1.4 Read day4.txt save tha in day4.txt to sting.txt file in custom folder (ex: "C:\Temp\sting.txt")'''


file = open('day4.txt','w')
file.write('This is day4')
file.write('this is done by: nimisha')
file.close()