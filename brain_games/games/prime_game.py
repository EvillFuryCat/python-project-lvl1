from random import randint


REGULATIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_start():
    number = randint(0, 100)
    question = f'{number}'
    if prime(number) == 'yes':
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def prime(number):
    if number == 2 or number == 3:
        return 'yes'
    if number % 2 == 0 or number < 2:
        return 'no'
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return 'no'
    return 'yes'
