"""user_text = input('Enter some text: ')

print(user_text.upper())

user_number = input("What do you want to double? ")

print(int(user_number) * 2)
"""
# Challenge: First ask for some text, and then prompt "Enter 1 to uppercase and 2 to lowercase:"

user_text = input("Enter some text: ")
user_opt = input("Select 1 for uppercase, 2 for lowercase. ")

for text in user_opt:
    if text == "1":
        print(user_text.upper())
    else:
        print(user_text.lower())

# Nicks way

if user_text == "1":
    print(user_text.upper())
else:
    print(user_text.lower())
