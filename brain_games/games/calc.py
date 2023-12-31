from brain_games.games.even import gen_numbers, get_answer, check_answer
from random import choice


DESCR = 'What is the result of the expression?'
NUM_ANSWER = True
PROGR_LEN = None


def give_question(_):
    rand_value_1, rand_value_2 = gen_numbers(2)
    signs = ('+', '-', '*')
    chosen_sign = choice(signs)
    print(f'Question: {rand_value_1} {chosen_sign} {rand_value_2}')
    return rand_value_1, chosen_sign, rand_value_2


def det_answer(iterable):
    num_1, num_2 = get_numbers(iterable)
    sign = get_sign(iterable)
    if sign == '+':
        result = num_1 + num_2
    elif sign == '-':
        result = num_1 - num_2
    else:
        result = num_1 * num_2
    return result


def get_numbers(iterable):
    return iterable[0], iterable[2]


def get_sign(iterable):
    return iterable[1]


get_answer = get_answer
check_answer = check_answer
