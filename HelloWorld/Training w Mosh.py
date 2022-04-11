# Shows your name and your favorite color
"""user = input("What is your name? ")
fav_color = input("What is your favorite color? ")
print(user + " likes " + fav_color)"""

# Shows how old you are to 2022
import math

"""birth_year = int(input("Birth Year: "))
print(type(birth_year))
age = 2022 - birth_year
print(type(age))
print(age)"""

# Pounds to Kilograms
"""
user_weight = int(input("What is your weight in pounds? "))
pounds_kilos = input("(L)bs or (K)g: ").upper()


if pounds_kilos == "L":
    convertor = user_weight * .45
    print(f"You are {convertor} in kilograms")
else:
    convertor = user_weight / .45
    print(f"You are {convertor} in pounds")
"""

# len function will display where a character is relative to the text. is below = 1
"""course = "Python for Beginners"
print(len("y"))
print(len(course) will show '20'. This is how many characters are in this text. 
# this is an index function and will show Pyt
print(course[0:3]) 
"""
# Using Triple quotes allows you to spread text out on multi lines
Welcome_email = """Hi Antoine,
Here is our first email to you. 

Thank you
The support team"""

# Formatted Strings.
"""
first = "John"
last = "Smith"
message = f"{first} {last} is a coder"
print(message)
"""

# Different methods you can use that modify your variable but not change it.
"""course = "Python for Beginners"
print(course.lower()) = python for beginners
print(course.upper()) = PYTHON FOR BEGINNERS
print(course.find("P")) = 0 
print(course.replace("P", "F")) = Fython for Beginners 
print("Python" in course) =  True
"""

# Math Operators
"""
print(10 + 3),      13 
print(10 * 3),      30
print(10 / 3),      3.33333333
print(10 // 3),     3
print(10 % 3),      1
x = 10 + 3 * 2,
print(x),           16
y = 2
y -= 2               This is a augmented math operator. can also write += or *= /=
print(y),            0
x = 2.9 
print(round(x)),    3  rounds the number 
print(abs(-2.9))    2.9 'absolute' always gives a positive number
print(math.ceil(2.9) 3 ceiling is giving the next value up.
print(math.floor(2.9) 2 floor is giving the next value down
Order of operation are:
(10 + 3) * 2 ** 2 = 52
parenthesis
exponentiation 
multiplication or division
addition or subtraction
"""
# Using logical if statements. Can look at Buying a House PY file for another example
"""
has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Income and Credit are Good")
    # Using the 'and' method must have both bullion's True or False

if has_high_income or has_good_credit:
    print("Income or Credit meets requirements")
    # Using the 'or' method can have either bullion's True or False

if has_good_credit and has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan, Please review records for more details")
    """


# Using While Loops
"""
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")
"""

