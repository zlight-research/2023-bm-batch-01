# 1. Create a txt file day4.txt
# 	1.1 write "This is day4" to day4.txt
# 	1.2 Read the same file, replace  "day4" with "4th day", save it on the same file
# 	1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file
# 		Output sample:
# 		This is 4th day
# 		This is done by : Yadhu
		
# 	1.4 Read day4.txt save tha in day4.txt to sting.txt file in custom folder(ex:"C:\Temp\sting.txt") 



file = open('day4.txt','w')  #Created a txt file day4.txt

file.write("This is day4") # writed "This is day4" to day4.txt

file = open('day4.txt','rt')
data=file.read()
data=data.replace('day4', '4th day') # replace  "day4" with "4th day"
file.close()
file = open('day4.txt','wt')  
file.write(data)
file.close()

file = open('day4.txt', 'a')
file.write("This is done by : Adarsh")#appended "This is done by : <name>"
file.close()

 

