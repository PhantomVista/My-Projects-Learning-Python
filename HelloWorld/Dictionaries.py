# Dictionaries are used to set values to a condition that we can call on

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": False
}
# ways to get this value
print(customer["name"])
print(customer.get("age"))

# ways to modify the dictionary
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

# Using a dictionary to modify a number
user = input("Phone: ")
numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

output = ""
for characters in user:
    output += numbers.get(characters) + " "
print(output)




