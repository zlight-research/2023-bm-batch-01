#Displayed as”Created my second program in Zlight Research Pvt Ltd”.
text="create my first program in research zlight"
#replace is used to change first to second
replace=text.replace("first", "second")
#split is used to separate all the words
split=text.split()
#capitalize is used to capitalize the first character in the string
split[0]=split[0].capitalize()
tem=split[6].capitalize()
split[6]=split[5].capitalize()
split[5]=tem
#convert the list to string
listToStr=' '.join([str(elem) for elem in split])
#print output
print(listToStr)