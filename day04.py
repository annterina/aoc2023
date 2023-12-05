import os
import re
import functools

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_card(line):
    match = re.match(r".*?:\s(.+?)\s\|\s(.+)$", line)
    winning = list(map(int, match.group(1).split()))
    numbers = list(map(int, match.group(2).split()))
    return winning, numbers


def points(game):
    winning = set(game[0])
    numbers = set(game[1])
    return 2 ** (len(winning & numbers) - 1) if len(winning & numbers) > 0 else 0


def main():
    filepath = f'{dir_path}/input/day04.txt'

    with open(filepath) as f:
        cards = list(map(lambda x: parse_card(x), f.read().strip().split('\n')))

    points_sum = functools.reduce(lambda acc, x: acc + points(x), cards, 0)

    print('Part 1: ')
    print(points_sum)

    winning_numbers = list(map(lambda game: len(set(game[0]) & set(game[1])), cards))

    # dict: index -> (quantity, winning_numbers)
    quantity_dict = {i+1: (1, winning_numbers[i]) for i in range(len(winning_numbers))}

    for card in range(1, len(winning_numbers) + 1):
        quantity, next_winner_range = quantity_dict[card]
        for next_winner in range(1, next_winner_range + 1):
            quantity_dict[card+next_winner] = \
                (quantity_dict[card + next_winner][0] + quantity, quantity_dict[card + next_winner][1])

    cards_number = functools.reduce(lambda acc, x: acc + x[0], quantity_dict.values(), 0)

    print('Part 2: ')
    print(cards_number)


if __name__ == '__main__':
    main()
