# This code will Generate random values

import random

for i in range(3):
    random.random()
    print(i)

# This code will generate a random # in range 10-20
for x in range(3):
    print(random.randint(10, 20))


# This code will generate random items

members = ['Goku', 'Krillen', 'Vageta', 'Broly']
leader = random.choice(members)
print(leader)
