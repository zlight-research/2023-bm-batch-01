"""
This is a sample code for conditon statement 'IF'

1 ) Check whether the given numbers are equal and if True, displays 'Number 1 and Number 2 are equal'
2 ) Check whether number 1 greater than number 2 and if True, displays 'Number 1 greater than Number 2'

"""

number_1 = 2
number_2 = 3
if number_1 == number_2:
    print('Number 1 and Number 2 are equal')

elif number_1 > number_2:
    print('Number 1 greater than Number 2')

elif number_1 < number_2:
    print('Number 1 less than Number 2')
else:
    print('Invalid number')

#  if else statement in single line ?


number_1 = 2
number_2 = 3
print('Number 1 less than Number 2') if number_1 < number_2 else print('Number 1 and Number 2 are equal')
