# Tuples are used whenever we do not want a list modified ()
# Tuples do not have call methods like list. They are immutable
# You can only get information from Tuples, not change them

numbers = (1, 2, 3)
print(numbers[0])

# Unpacking is getting a value from a list/tuple and storing it in a variable
# There are several ways to unpack. In Python there's a simple way.

coordinates = (1, 2, 3)

# other programs way to unpack
"""
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
"""

# Pythons way to unpack

x, y, z = coordinates
print(x)

