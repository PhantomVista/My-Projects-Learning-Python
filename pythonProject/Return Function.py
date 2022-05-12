def double(number):
    return number * 2

new_number = double(200)

print(new_number)

# Challenge: create a function that returns a string in all carps


def uppercase(text):
    return text.upper()


print((uppercase("google")))

# Note on below. If you don't make your variable a list, you will see different results in your for loop.
names = ["paul, gary, frank"]

for name in names:
    print(uppercase(name))



