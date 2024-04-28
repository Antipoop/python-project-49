from brain_games.cli import welcome_user

def logic(game):
    user_name = welcome_user()
    game.rule()
    rounds = 3
    i = 0
    while i < rounds:
        result_game = game.run()
        correct_answer = result_game["answer"]
        question = result_game["question"]
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")
            return
        print('Correct!')
        i += 1
    print(f'Congratulations, {user_name}!')