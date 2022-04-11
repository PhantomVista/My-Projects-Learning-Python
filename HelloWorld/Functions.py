# Using the def function. This is used to call on a line of code at any time
# The order of calling the functions matter. Must call function after def line
"""
def great_user():
    print('Hi there!')
    print('Welcome aboard!')

print("Start")
great_user()
print('Finish')
"""

# using an input parameter in function to call on anytime
# parameter - placeholders/local variable inside the def function
"""
def greet_user(name):
    print(f'Hi {name}')
    print('Welcome aboard')
"""
# Note, by added a parameter, you must provide an 'argument' to the function
# argument - is the variable inside the function after calling it. You can not
# leave the function blank once a parameter is set.

"""
print('Start')
greet_user("Angie")
greet_user("Aria")
print('Finish')

Start
Hi Angie
Welcome aboard
Hi Aria
Welcome aboard
Finish """

# Positional Arguments vs keyword argument
# Passing the keyword will let Python know the order you want to show first
# The keyword argument must come after the positional argument if mixing them.


def greet_user(first_name, last_name):
    print(f'{first_name} {last_name}!')
    print('Welcome aboard')


print('Start')
greet_user("Mary", last_name="Jane")
print('Finish')
