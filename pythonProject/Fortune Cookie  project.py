import random

lucky_number = random.randint(5, 10)

fortune_number = random.randint(1, 3)

fortune_text = ""

if fortune_number == 1:
    fortune_text = "Today someone sexy pursues you, demanding to hangout with you!"
if fortune_number == 2:
    fortune_text = "Today someone cute pursues you, shyly asking to hangout with you!"
if fortune_number == 3:
    fortune_text = "Today someone hot pursues you, she flirts a lot, dropping sexual hints to you!"


print(f"{fortune_text} Your pursuer attractiveness is a level: {lucky_number}")

