"""Text = “created my first program in research zlight”
Replace the text “first” to “second”
Swap the words research and zlight
Displayed as”Created my second program in Zlight Research Pvt Ltd” """


#1
txt = "I created my first program in research zligh"

x = txt.replace("first", "second")

print(x)


#2
sentence = "Created my first program in research zlight Pvt Ltd"
words = sentence.split()
words[5], words[6] = words[6], words[5]
new_sentence = " ".join(words)
print(new_sentence)
