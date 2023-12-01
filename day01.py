import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def to_digit(line):
    first = next(filter(lambda x: x.isdigit(), line))
    last = next(filter(lambda x: x.isdigit(), line[::-1]))
    return int(first + last)


text_digits = {"oneight": 18, "twone": 21, "threeight": 38, "fiveight": 58, "sevenine": 79,
               "eightwo": 82, "eighthree": 83, "nineight": 98, "one": 1, "two": 2, "three": 3,
               "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def to_digit_with_text(line):
    replaced = line
    for word, digit in text_digits.items():
        replaced = replaced.replace(word, str(digit))
    return to_digit(replaced)


def main():
    filepath = f'{dir_path}/input/day01.txt'

    with open(filepath) as f:
        numbers = list(map(lambda x: to_digit(x), f.read().strip().split('\n')))

    print('Part 1: ')
    print(sum(numbers))

    with open(filepath) as f:
        numbers = list(map(lambda x: to_digit_with_text(x), f.read().strip().split('\n')))

    print('Part 2: ')
    print(sum(numbers))


if __name__ == '__main__':
    main()
