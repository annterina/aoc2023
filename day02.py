import os
import re
import functools

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_cubes(cubes):
    red = re.findall(r'\d+ red', cubes)
    blue = re.findall(r'\d+ blue', cubes)
    green = re.findall(r'\d+ green', cubes)
    return {
        'red': int(red[0].split(' red')[0]) if red else 0,
        'blue': int(blue[0].split(' blue')[0]) if blue else 0,
        'green': int(green[0].split(' green')[0]) if green else 0,
    }


def max_cubes(cubes_dicts):
    max_values = {'red': 0, 'blue': 0, 'green': 0}
    for cube in cubes_dicts:
        for color in max_values:
            max_values[color] = max(max_values[color], cube[color])
    return max_values


def parse_game(line):
    game = line.split(': ')
    game_id = int(game[0].split('Game ')[1])
    cubes = game[1].split('; ')
    cubes_dicts = list(map(parse_cubes, cubes))
    return game_id, max_cubes(cubes_dicts)


constraints = {'red': 12, 'blue': 14, 'green': 13}


def main():
    filepath = f'{dir_path}/input/day02.txt'

    with open(filepath) as f:
        games_tuples = list(map(lambda x: parse_game(x), f.read().strip().split('\n')))

    games = dict((game_id, cubes) for game_id, cubes in games_tuples)

    game_ids_sum = 0
    for game_id, cube_dicts in games.items():
        if all(cube_dicts[color] <= constraints[color] for color in constraints):
            game_ids_sum += game_id

    print('Part 1: ')
    print(game_ids_sum)

    cubes_power = 0
    for game_id, cube_dicts in games.items():
        cubes_power += functools.reduce(lambda x, y: x * y, cube_dicts.values(), 1)

    print('Part 2: ')
    print(cubes_power)


if __name__ == '__main__':
    main()
