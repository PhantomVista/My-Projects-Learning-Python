# Rock, paper and scissors game in Python

from random import randint
choices = ["rock", "paper", "scissors"]
playGame = True

while playGame is True:

    computer = choices[randint(0, 2)]
    player = input("Choose rock, paper, or scissors? ").lower()

    if computer == player:
        print("Tie!")

    elif player == "rock":
        if computer == "scissors":
            print("You win! Rock smashed scissors.")
        else:
            print("You lose. Paper covers rock.")

    elif player == "paper":
        if computer == "rock":
            print("You win! Paper cover rock!")
        else:
            print("You lose. Scissors cuts paper.")

    elif player == "scissors":
        if computer == "scissors":
            print("You win! Scissors cuts paper")

    else:
        print("Not a valid play. Check your spelling and try again.")

    keepPlaying = input("Play again? ").lower()

    if keepPlaying == "no".lower():
        playGame = False
        print("Thanks for Playing!")
    elif keepPlaying == "yes".lower():
        playGame = True
    else:
        print("Not a valid play. Please type 'Yes' or 'No'")
