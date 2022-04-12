# Using 2 dimensional matrix. Mostly used in Machine Learning

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][1])

# This is using a loop to see all the items in the matrix
"""
for row in matrix:                                          
    for item in row:
        print(item)
"""

# Using Methods on your list
numbers = [2, 4, 6, 1, 3, 5, 2]

# this will add 0 to the last position of your list
numbers.append(0)
print(numbers)

# this will add a number in the first (0) position the new # (9)
numbers.insert(0, 9)
print(numbers)

# this method will remove an item from you list
numbers.remove(6)
print(numbers)

# this will remove the last item on your list
numbers.pop()
print(numbers)

# This will check the first occurrence of the item in your list/
# Or use the 'in' function to see if this item is true or false
print(numbers.index(4))
print(3 in numbers)

# This will check to see how many times this item appears on the list
print(numbers.count(2))

# This will sort your list automatically
numbers.sort()
print(numbers)

# This will reverse your list
numbers.reverse()
print(numbers)

# This method gives you the copy of the original list
numbers2 = numbers.copy()
print(numbers2)

# this will remove all the items on your list
numbers.clear()
print(numbers)


