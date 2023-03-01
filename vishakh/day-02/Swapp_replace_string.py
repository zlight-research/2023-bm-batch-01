'''
3.) Text = “created my first program in research zlight”

Replace the text “first” to “second”

Swap the words research and zlight

 
Displayed as”Created my second program in Zlight Research Pvt Ltd”.


'''

#Assigning a string value into a variable

text="created my first program in research zlight"
print(text)

#the string value 'first' can be replace to 'second' to using replace function and display it

replace_text=text.replace("first","second")
print(replace_text)

#the string  values split by special charecter 'space' to convert to list
split_text=replace_text.split(' ')
print(split_text)

#swapping two values in the list 'research' and 'zlight' using their index
word1,word2=split_text.index('research'),split_text.index('zlight')
split_text[word2],split_text[word1]=split_text[word1],split_text[word2]
print(split_text)

#change case of first letter of some words in list using their index and title() function

split_text[0],split_text[5],split_text[6]=split_text[0].title(),split_text[5].title(),split_text[6].title()
print(split_text)


#list can be converted to string

list_to_string= ' '.join(split_text)
print(list_to_string)


print("*"*100)
#adding new string and display the final output
new_string='Pvt Ltd'
final_output=" ".join([list_to_string,new_string])
print(final_output) 

 