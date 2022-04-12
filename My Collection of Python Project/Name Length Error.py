name = input("Enter Your Name: ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name is too long. Max 50 Characters")
else:
    print("Name Looks Good")


