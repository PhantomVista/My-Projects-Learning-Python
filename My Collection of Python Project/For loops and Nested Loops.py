# For Loops. This code will print the sum of the list of prices.
prices = [10, 20, 30]

items = 0
for stuff in prices:
    items += stuff
print(items)
print("""
""")
# Nested loops

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
print("""
""")
# Drawing a Letter F with Loops. For loops and Nested loops examples.

numbers = [5, 2, 5, 2, 2]
for things in numbers:
    print(things * "x")

print("""
""")

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += "x"
    print(output)

print("""
""")

# Printing a L
number = [1, 1, 1, 1, 5]
for l_count in number:
    outputs = ""
    for counts in range(l_count):
        outputs += "x"
    print(outputs)

