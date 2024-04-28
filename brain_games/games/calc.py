import random


def rule():
    print('What is the result of the expression?')


def run():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.randint(1, 3)
    match operation:
        case 1:
            correct_answer = f'{num1 + num2}'
            str_operation = f'{num1} + {num2}'
        case 2:
            correct_answer = f'{num1 - num2}'
            str_operation = f'{num1} - {num2}'
        case 3:
            correct_answer = f'{num1 * num2}'
            str_operation = f'{num1} * {num2}'
    return {'question': str_operation, 'answer': correct_answer}
