"""3.       Text = “created my first program in research zlight”

Replace the text “first” to “second”

Swap the words research and zlight

Displayed as”Created my second program in Zlight Research Pvt Ltd”.
"""


text = "create my first program in research zlight"
replace = text.replace("first", "second")
person = text.split()  # separate all the words
person[0] = person[0].title()  # title() converted to upper case
tem = person[6].title()
person[6] = person[5].title()
person[5] = tem
print(" ".join(person))
