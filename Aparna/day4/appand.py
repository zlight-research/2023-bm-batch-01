# 1.3 Read the same file, append "This is done by : <Your_name>" , save it on the same file
# 		Output sample:
# 		This is 4th day
# 		This is done by : Yadhu

file = open('write.txt','a')
file.write('This is day4')
file.write('this is done by: aparna')
file.close()
