# Using list. With Nick Walter

fav_movies = ["Vanilla Sky", "Marvel Avengers: End Game", "The Matrix"]
print(fav_movies[2])

# Challenge: Make a list of your 3 favorite numbers and print the first number from your list

fav_numbers = [69, 1, 99]
print(fav_numbers[0])

print(len(fav_movies))

fav_movies.append("Sonic")
print(fav_movies)
print(len(fav_movies))
fav_movies.insert(1, "Superman")
print(fav_movies)
del(fav_movies[2])
print(fav_movies)

# Challenge: Delete all movies from list using code until 1 is left
del(fav_movies[1:4])
print(fav_movies)