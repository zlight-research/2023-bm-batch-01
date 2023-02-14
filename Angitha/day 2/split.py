"""How to split the names in based on special character"""

# company="First_word =Zlight\nSecond Word =Research\n"
# """\n become newline"""
# print(company)

input ="zlight research"
words=input.split()

print("First_word=",words[0].capitalize())

print("Second Word=",words[1].capitalize())    


