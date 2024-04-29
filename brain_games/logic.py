import prompt


def logic(game, rounds):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    game.rule()
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
