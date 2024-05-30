import random


def create_random_numbers():
    return random.sample(range(0, 91), 25)


def create_bingo_list(card_numbers):
    bingo_list = []
    for i in range(0, len(card_numbers), 5):
        row = card_numbers[i: i + 5]
        row.sort()
        bingo_list.append(row)
    bingo_list[2][2] = 'bingo'

    return bingo_list


def print_bingo_card(bingo_list):
    print('-' * 51)
    for row in bingo_list:
        print('|', ' | '.join(f"{str(num):^7}" for num in row), '|')
        print('-' * 51)
    return bingo_list


def create_bingo_card():
    return print_bingo_card(create_bingo_list(create_random_numbers()))


create_bingo_card()
