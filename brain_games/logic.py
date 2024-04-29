from brain_games.cli import welcome_user
import prompt


def logic(game):
    user_name = welcome_user()
    game.rule()
    rounds = 3
    i = 0
    while i < rounds:
        result_game = game.run()
        correct = result_game["answer"]
        question = result_game["question"]
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct:
            str1 = f"'{answer}' is wrong answer ;(. "
            str2 = f"Correct answer was '{correct}'."
            print(str1 + str2)
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
        i += 1
    print(f'Congratulations, {user_name}!')
