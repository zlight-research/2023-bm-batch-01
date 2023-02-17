f=open("textfile.txt",'r')
#readline-is to read the first line
print(f.readline())

f=open("textfile.txt",'r')
string=f.readline()
# replace is used to replace the occurance of string with another string
print(string.replace('day4','4th day'))

f=open("textfile.txt",'r')
string=f.read()
print(string.replace('day4','4th day'))