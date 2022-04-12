# Pounds to Kilograms

user_weight = int(input("What is your weight in pounds? "))
pounds_kilos = input("(L)bs or (K)g: ").upper()


if pounds_kilos == "L":
    convertor = user_weight * .45
    print(f"You are {convertor} in kilograms")
else:
    convertor = user_weight / .45
    print(f"You are {convertor} in pounds")
