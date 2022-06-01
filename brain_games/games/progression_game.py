from random import randint


REGULATIONS = "What number is missing in the progression?"


def get_start():
    first_border = randint(0, 100)
    step_progression = randint(3, 27)
    length_question = 10
    second_border = first_border + (step_progression * length_question)
    progression = []
    for i in range(first_border, second_border, step_progression):
        progression.append(str(i))

    index_hidden_number = randint(0, length_question - 1)
    correct_answer = progression[index_hidden_number]
    progression[index_hidden_number] = ".."
    question = ' '.join(progression)
    return question, correct_answer
