numbers = [2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9]
no_dup = []
for item in numbers:
    if item not in numbers:
        no_dup.append(item)
print(no_dup)

