import os
import functools

dir_path = os.path.dirname(os.path.realpath(__file__))


def calculate_distances(time, record):
    distances = [(time - speed) * speed for speed in range(time + 1)]
    return [distance for distance in distances if distance > record]


def main():
    filepath = f'{dir_path}/input/day06.txt'

    with open(filepath) as f:
        lines = f.read().strip().split('\n')

        times = list(map(int, lines[0].split()[1:]))
        distances = list(map(int, lines[1].split()[1:]))
        races = list(zip(times, distances))

        possibilities = list(map(lambda race: calculate_distances(race[0], race[1]), races))
        result = functools.reduce(lambda acc, poss: acc * len(poss), possibilities, 1)

        print('Part 1:')
        print(result)

        time = 40829166
        distance = 277133813491063
        possibilities = calculate_distances(time, distance)

        print('Part 2:')
        print(len(possibilities))


if __name__ == '__main__':
    main()
