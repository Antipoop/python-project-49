import random

def rule():
    print('What number is missing in the progression?')


def get_progression(start, length, diff):
    progression = []
    i = 0
    while i < length:
        num = start + diff * i
        progression.append(str(num))
        i += 1
    return progression


def run():
    progression_length = random.randint(5, 10)
    progression_diff = random.randint(1, 15)
    start_item = random.randint(0, 100)
    hidden_num = random.randint(0, progression_length - 1)
    progression = get_progression(start_item, progression_length, progression_diff)
    correct_answer = progression[hidden_num]
    progression[hidden_num] = '..'
    str_progression = ' '.join(progression)
    return { 'question': str_progression, 'answer': correct_answer }