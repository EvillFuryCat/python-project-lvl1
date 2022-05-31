'''Логика выполнения игр'''
import prompt


ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.REGULATIONS)
    for _ in range(ROUNDS):
        random_number, correct_answer = game.is_even()
        print(f'Question: {random_number}')
        user_answer = prompt.string("Your answer: ")
        if user_answer.lower() == correct_answer.lower():
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(."
                  f" Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
