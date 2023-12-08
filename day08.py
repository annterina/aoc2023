import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_element(line):
    key, values = line.split(' = ')
    left, right = values[1:-1].split(', ')
    return key, (left, right)


def traverse(code, elements, current='AAA', end='Z'):
    for i, step in enumerate(code * 100):
        current = elements[current][0] if step == 'L' else elements[current][1]
        if current.endswith(end):
            return i + 1


def main():
    filepath = f'{dir_path}/input/day08.txt'

    with open(filepath) as f:
        lines = lines = f.read().strip().split('\n\n')

    code = lines[0]
    elements = dict(list(map(lambda x: parse_element(x), lines[1].split('\n'))))

    print('Part 1:')
    print(traverse(code, elements))

    starts = ['AAA', 'MGA', 'DGA', 'TLA', 'RDA', 'DPA']
    cycles = list(map(lambda x: traverse(code, elements, x, 'Z'), starts))

    print('Part 2:')
    print(math.lcm(*cycles))


if __name__ == '__main__':
    main()
