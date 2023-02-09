'''
1)how to split the names in based on special charecter
eg: input="zlight research"
Assign to 2 variables,Displayed as a given below
First_word=Zlight
second word =Research

'''


#Assigning a string into variable and display it

name_of_string="Zlight Research"
print(name_of_string)

#split the string using special charecter ' ' (space) used with split fuction and display it

split_string=name_of_string.split(' ')
print(split_string)

#splitting words are assign to 2 variables and display it

First_word,Second_word=split_string[0],split_string[1]
print("First WORD is:",First_word)
print("Second word is:",Second_word)

