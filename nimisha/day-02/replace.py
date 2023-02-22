'''Text = “created my first program in research zlight”

Replace the text “first” to “second”

Swap the words research and zlight
Displayed as”Created my second program in Zlight Research Pvt Ltd”.'''

# entering the given value to the variable
text ="created my first program in research zlight"
# replace() func is used to replace the given word
new_text =text.replace("first","second")

print(" text = " ,new_text)
# finally printing the replaced word
text2="created my second program in research zlight pvt ltd"
swaping=text2.split()
swaping[5], swaping[6]= swaping[6], swaping[5]
new_text2="". join(swaping)
print(new_text2)