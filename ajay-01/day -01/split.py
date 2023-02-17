1.#       How to split the names in based on special character
#Eg:
#Input = “zlight research”
#Assign to 2 variables, Displayed as given below
#First_word = Zlight
#Second Word = Research

#variable declaration
name="zlight reaserch"
print(name)
#split() function used.
name_1=name.split()
print("First_word=",name_1[0])
print("second_word=",name_1[1])