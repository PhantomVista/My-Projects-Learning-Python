def find_max(numbers):
    biggest_number = numbers[0]
    for number in numbers:
        if number > biggest_number:
            biggest_number = number
    return biggest_number


