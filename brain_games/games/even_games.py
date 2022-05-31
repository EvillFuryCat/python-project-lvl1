from random import randint


REGULATIONS = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER_RANGE = 1
MAX_NUMBER_RANGE = 100


def get_start():
    random_number = randint(MIN_NUMBER_RANGE, MAX_NUMBER_RANGE)
    question = random_number
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
