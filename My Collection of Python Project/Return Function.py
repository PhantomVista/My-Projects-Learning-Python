# Using the Return function is best for calculating within a def.
# You can still use the print command w/o return, but you will see 'None'


def square(number):
    return number * number


print(square(3))

# How to handle errors by using 'try' 'except'
# Using the try except method will tell your pgm to try this pgm and except
# the error that may happen if the user typed an incorrect value

try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
    print(risk)
except ValueError:
    print('Invalid Value')

