#4)Accept boolean variable and display "F" fOR False "M for True"


bool_data=input("enter a bool value")#input a boolean value(True or False)

if bool_data=='True':
    print("M")#STATEMENT IS TRUE THEN PRINT "M"
elif bool_data=='False':
    print("F")  #STATEMENT IS FALSE THEN PRINT"F"  

else:
    print("it is not a boolean value")