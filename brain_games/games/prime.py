import random


def rule():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def run():
    num = random.randint(1, 100)
    answer = 'yes'
    if num < 2:
        answer = 'no'
    i = 2
    while i < num:
        if num % i == 0:
            answer = 'no'
        i += 1
    return {'question': num, 'answer': answer}
