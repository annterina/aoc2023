import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def extrapolate(history, direction='forwards'):
    if all(number == 0 for number in history):
        return 0
    else:
        differences = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        if direction == 'forwards':
            return history[-1] + extrapolate(differences, direction)
        else:
            return history[0] - extrapolate(differences, direction)


def main():
    filepath = f'{dir_path}/input/day09.txt'

    with open(filepath) as f:
        histories_lines = f.read().strip().split('\n')

    histories = list(map(lambda x: list(map(lambda number: int(number), x.split())), histories_lines))

    next_values = []
    for history in histories:
        next_values.append(extrapolate(history))

    print('Part 1:')
    print(sum(next_values))

    next_values = []
    for history in histories:
        next_values.append(extrapolate(history, 'backwards'))

    print('Part 2:')
    print(sum(next_values))


if __name__ == '__main__':
    main()
