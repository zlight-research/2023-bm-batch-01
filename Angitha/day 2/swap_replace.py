"""Text = “created my first program in research zlight”
Replace the text “first” to “second”
Swap the words research and zlight
Displayed as”Created my second program in Zlight Research Pvt Ltd” """


"""Replace the text “first” to “second” """
company =" created my first program in research zlight"
wrk=company.replace("first","second")
"""In this replace to use new wrd can display"""
print(wrk)


"""Swap the words research and zlight"""
company="created my first program in research zlight"
words=company.split()
"""split sentence into words"""
words[5],words[6]=words[6],words[5]
"""swap research and zlight"""
new_sentence=" ".join(words)
"""convert into strings"""
print(new_sentence)

