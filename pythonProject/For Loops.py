for number in range(10):
    print("Hello")
    print(number)

fav_movies = ["Vanilla Sky", "Marvel Avengers: End Game", "The Matrix"]
for movies in fav_movies:
    print(movies)

# Challenge: Loop 40 times and print number of loops 2. Ex: 2, 4, 6,8

x = 1
for numbers in range(40):
    numbers *= x * 2
    print(numbers)

# Nicks way (gets rid of the zero)

for number in range(40):
    print((number + 1) * 2)

