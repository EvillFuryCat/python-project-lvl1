from random import randrange
from random import choice


REGULATIONS = 'What is the result of the expression?'


def get_start():
    first_number = randrange(0, 30)
    second_number = randrange(0, 30)
    operators = choice('+-*')
    question = (f'{first_number} {operators} {second_number}')
    correct_answer = str(eval(f'{first_number}{operators}{second_number}'))
    return question, correct_answer
