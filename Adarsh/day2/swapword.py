#3) Displayed as Text = “created my first program in research zlight”

"""Created my second program in Zlight Research Pvt Ltd"""

text = "Created my first program in research zlight"
replace=text.replace("first", "second") #replaced word by second
split = replace.split()  # splitted all the words
split[0] = split[0].title()  # title() to convert to upper case

#------swapping  the word------

temp = split[6].title()
split[6] = split[5].title()
split[5] = temp
#---------------------------------
final=" ".join(split) #joined the splitted words as a string
print(final,"Pvt Ltd") #Display the final result


