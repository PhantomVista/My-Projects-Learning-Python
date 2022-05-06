# LinkedIn Learning Course for Python Cert. Free w/ Library Card : )
# https://www.linkedin.com/learning/python-for-non-programmers/your-first-line-of-code?autoSkip=true&autoplay=true&contextUrn=urn%3Ali%3AlyndaLearningPath%3A5f6cf9fe498e1b8929698639&resume=false&u=95224169
# Optional: use an online site for coding python Replit

print("Hello World")


# Recursion - a thing that included itself. In programing, when a function calls itself
"""
def shortest():
    shortest()

shortest()
"""
# This is the simple form of recursion, this will create a recursion error.

# Example of stacking.
spam = []
spam.append('Alice')
spam.append('Bob')
spam.append('Carol')
spam.pop()

print(spam)

# Another example of stacking. None of these would work after a() until we def the next.
def a():
    print('Start of a()')
    b()
    print('End of a()')
def b():
    print('Start of b()')
    c()
    print('End of b()')
def c():
    print('Start of C()')
    print('End of c()')


a()

# Factorial examples


def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))


# Recursive Fibonacci


def fib(nthNumber):
    if nthNumber == 1 or nthNumber == 2:
        return 1
    else:
        return fib(nthNumber - 2) + fib(nthNumber - 1)


fib(nthNumber=10)


