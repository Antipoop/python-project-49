import random


def rule():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def run():
    num = random.randint(1, 100)
    match num % 2 == 0:
        case True:
            correct_answer = 'yes'
        case False:
            correct_answer = 'no'
    return {'question': num, 'answer': correct_answer}
