import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(2)
print("Picking a number...")
time.sleep(2)
guess = int(input("Number selected, what is your guess? "))
correct_number = random.randint(1, 100)
guess_count = 1


while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong, You need to guess higher. What is your guess? "))
    else:
        guess = int(input("Wrong, You need to guess lower. What is your guess? "))
    if guess_count >= 14:
        print("Sorry, no more guesses for you")
        break
    if guess == correct_number:
        print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses")
        break
print("THANKS FOR PLAYING")
