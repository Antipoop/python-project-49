from brain_games.cli import welcome_user
import random

def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = random.randint(1, 100)
        match num % 2 == 0:
            case True:
                correct_answer = 'yes'
            case False:
                correct_answer = 'no'
        print(f'Question:{num}')
        user_answer = input('Your answer:')
        if correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return
        print('Correct!')
        i += 1
    print(f'Congratulations, {name}!')

def main():
    return brain_even()
