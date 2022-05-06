import random

print(random.randint(1, 10))

print(random.random())

# Challenge: Make your own version of a magic 8-ball that prints yes, no, or maybe each time you ask it
a = "yes"
b = "no"
c = "maybe"

print(random.choice(({a}, {b}, {c})))

# Nicks way of handling the challenge
answer = random.randint(1, 3)

if answer == 1:
    print("Yes")
elif answer == 2:
    print("No")
else:
    print("Maybe")

