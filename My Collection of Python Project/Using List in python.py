# Using list to get the sum of total
prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f"Total: {total}")

# Using list to update names in a list
names = ['Vegeta', 'Goku', 'Broly', 'Kale']
print(names[2:])
names[1] = "Kakorot"
print(names)

# Using list to find the largest number in a list

# My way
numbers = [1, 2, 3, 100, 4, 5, 88]
x = max(numbers)
print(x)

# Moshes Way

maxed = numbers[0]
for numbers in numbers:
    if numbers > maxed:
        maxed = numbers
print(maxed)


