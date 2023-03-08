
#1. Create a txt file day4.txt
f=open("G:\2023-bm-batch-01\Syam saleel\day-04\day4.txt","w")
#1.1 write "This is day4" to day4.txt
f.write("This is day4")
#1.2 Read the same file, replace  "day4" with "4th day", save it on the same file4
f=open("G:\2023-bm-batch-01\Syam saleel\day-04\day4.txt","r+")
z=f.read()
z=z.replace("day4", "4th day\n")
f.write(z)
""" When you open a file in read mode ("r"), you can only read its contents, 
but you cannot write to it. To make changes to the contents of a file, 
you need to open it in write mode ("w") or read-write mode ("r+")."""
f.write("This is done by :Syam")


#
file_1 = open("G:\\2023-bm-batch-01\\Syam saleel\\day-04\\day4.txt", "r")
contents = file_1.read()
file_1.close()

#
file_2 = open("G:\\2023-bm-batch-01\\\\Syam saleel\\day-04\\sting.txt", "w")
file_2.write(contents)
file_2.close()
