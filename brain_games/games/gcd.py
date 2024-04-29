import random


def rule():
    print('Find the greatest common divisor of given numbers.')


def run():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    numbers = f'{num1} {num2}'
    i = 1
    while i <= min(num1, num2):
        if min(num1, num2) % i == 0 and max(num1, num2) % i == 0:
            answer = f'{i}'
        i += 1
    return {'question': numbers, 'answer': answer}
