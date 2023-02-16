#Text = “created my first program in research zlight”

#Replace the text “first” to “second”

#Swap the words research and zlight
 
#Displayed as”Created my second program in Zlight Research Pvt Ltd”.
 
Text="created my first program in research zlight"
Text_replace=Text.replace("first","second")
# Swap the word reserch and zlight
words=Text.split()
words[5],words[6]=words[6],words[5]
Text = " ".join(word.capitalize() for word in words)
Text += " Pvt Ltd"
print(Text)


