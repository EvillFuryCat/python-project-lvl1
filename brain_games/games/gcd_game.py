from random import randrange

REGULATIONS = "Find the greatest common divisor of given numbers."


def get_start():
    first_number = randrange(1, 40)
    second_number = randrange(1, 40)
    question = f'{first_number} {second_number}'
    while first_number != 0 and second_number != 0:
        if first_number >= second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    correct_answer = first_number or second_number
    return question, str(correct_answer)
