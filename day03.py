import os
import re
import itertools

dir_path = os.path.dirname(os.path.realpath(__file__))


symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';',
           ':', '\'', '"', ',', '<', '>', '/', '?', '`', '~']


# dict: row -> [col, col, col, ...]
def parse_symbols(row, line):
    columns = [i for i, char in enumerate(line) if char in symbols]
    return row, columns


# dict: row -> [col, col, col, ...]
def parse_stars(row, line):
    columns = [i for i, char in enumerate(line) if char == '*']
    return row, columns


# dict: row -> [(min_col, max_col, value), (min_col, max_col, value), ...]
def parse_numbers(row, line):
    pattern = re.compile(r'(\d+)')
    matches = pattern.finditer(line)
    numbers = [(match.start(), match.end() - 1, int(match.group())) for match in matches]
    return row, numbers


def main():
    filepath = f'{dir_path}/input/day03.txt'

    with open(filepath) as f:
        symbols = list(map(lambda x: parse_symbols(*x), enumerate(f.read().strip().split('\n'))))

    with open(filepath) as f:
        numbers = list(map(lambda x: parse_numbers(*x), enumerate(f.read().strip().split('\n'))))

    symbols_dict = dict((row, columns) for row, columns in symbols)
    numbers_dict = dict((row, numbers) for row, numbers in numbers)

    parts = []
    for row, numbers in numbers_dict.items():
        for min_col, max_col, value in numbers:
            symbol_columns = [symbols_dict.get(symbol_row, []) for symbol_row in range(row - 1, row + 2)]
            digit_columns = [*range(min_col - 1, max_col + 2)]
            if list(set(itertools.chain(*symbol_columns)) & set(digit_columns)):
                parts.append(value)

    print('Part 1: ')
    print(sum(parts))

    with open(filepath) as f:
        stars = list(map(lambda x: parse_stars(*x), enumerate(f.read().strip().split('\n'))))

    stars_dict = dict((row, columns) for row, columns in stars)

    gears = []
    for row, columns in stars_dict.items():
        numbers = [numbers_dict.get(number_row, []) for number_row in range(row - 1, row + 2)]
        flatten_numbers = itertools.chain(*numbers)
        number_columns = [([*range(number[0] - 1, number[1] + 2)], number[2]) for number in flatten_numbers]
        for column in columns:
            close_numbers = list(filter(lambda number: column in number[0], number_columns))
            if len(close_numbers) == 2:
                gears.append(close_numbers[0][1] * close_numbers[1][1])

    print('Part 2: ')
    print(sum(gears))


if __name__ == '__main__':
    main()
