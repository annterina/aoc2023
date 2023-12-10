import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def max_in_pipe(matrix, coordinates, max=1, direction='north'):
    row, column = coordinates

    while True:
        value = matrix[row][column]

        if value == '|':
            if direction == 'north':
                row -= 1
            elif direction == 'south':
                row += 1
            else:
                break
        elif value == '-':
            if direction == 'west':
                column -= 1
            elif direction == 'east':
                column += 1
            else:
                break
        elif value == 'J':
            if direction == 'east':
                row -= 1
                direction = 'north'
            elif direction == 'south':
                column -= 1
                direction = 'west'
            else:
                break
        elif value == 'L':
            if direction == 'west':
                row -= 1
                direction = 'north'
            elif direction == 'south':
                column += 1
                direction = 'east'
            else:
                break
        elif value == 'F':
            if direction == 'west':
                row += 1
                direction = 'south'
            elif direction == 'north':
                column += 1
                direction = 'east'
            else:
                break
        elif value == '7':
            if direction == 'east':
                row += 1
                direction = 'south'
            elif direction == 'north':
                column -= 1
                direction = 'west'
            else:
                break
        else:
            break
        max += 1
    return max


def main():
    filepath = f'{dir_path}/input/day10.txt'

    with open(filepath) as f:
        rows = f.read().strip().split('\n')

    matrix = [list(row) for row in rows]

    start_coordinates = None
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == 'S':
                start_coordinates = (i, j)
                break

    max_loop = max_in_pipe(matrix, (start_coordinates[0] - 1, start_coordinates[1]))
    print('Part 1:')
    print(int(max_loop/2))


if __name__ == '__main__':
    main()
