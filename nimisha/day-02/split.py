'''1.How to split the names in based on special character

Eg:

Input = “zlight research”

Assign to 2 variables, Displayed as given below'''

#assigning the characters
word="zlight research" #'word' is variable storing unit

#using split() function to split the word 
new=word.split()
print(word)
#to print the splitted words
print("firstword:",new[0].title())
print("secondword:",new[1].title())

 