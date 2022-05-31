from random import randint


REGULATIONS = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER_RANGE = 1
MAX_NUMBER_RANGE = 100


def is_even():
    random_number = randint(MIN_NUMBER_RANGE, MAX_NUMBER_RANGE)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
