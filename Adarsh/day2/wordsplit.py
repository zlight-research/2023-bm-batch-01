'''' 1) How to split the names in based on special character
Eg:Input = “zlight research”
Assign to 2 variables, Displayed as given below
First_word = Zlight
Second Word = Research'''
 
name = input("Enter the name:")  # Input the name
split = name.split() #for splitting the word
first_word = split[0].capitalize() #store first word 
second_word = split[1].capitalize() #store second word
print("first_word=",first_word)  #print first word 
print("second_word=",second_word) #print second word 