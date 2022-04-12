# Importing from utils file to using the def function.

import utils

# create any numbers in the list below, and it will find the biggest one
numbers = [23, 4, 5, 6]

print(utils.find_max(numbers))

# Second way to do it is like this

from utils import find_max

print(find_max(numbers))
