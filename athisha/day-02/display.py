"""3.       Text = “created my first program in research zlight”

Replace the text “first” to “second”

Swap the words research and zlight

Displayed as”Created my second program in Zlight Research Pvt Ltd”.
"""

text1 = "create my first program in research zlight"
# Replace "first" with "second"
text1 = text1.replace("first", "second")  
# Swap "research" and "zlight"
text1 = text1.replace("research zlight", "Zlight Research Pvt Ltd")
# Split the text1
person = text1.split() 
person[0] = person[0].capitalize() # Capitalize the first letter of the sentence 
tem = person[6].capitalize()
person[6] = person[5].capitalize()
person[5] = tem
print(" ".join(person))
