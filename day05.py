import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def dict_key_value(destination, source, quantity):
    return (int(source), int(source) + int(quantity) - 1), int(destination) - int(source)


def seed_range(seed_pair):
    return seed_pair[0], seed_pair[0] + seed_pair[1] - 1


def calculate_from_maps(point, maps):
    for map_dict in maps:
        for (start, end), change in map_dict.items():
            if start <= point <= end:
                point += change
                break
    return point


def dest_to_source_map(source_to_dest_map):
    dest_to_source_map = {}
    for (start, end), change in source_to_dest_map.items():
        dest_to_source_map[(start + change, end + change)] = change * (-1)
    return dest_to_source_map


def main():
    filepath = f'{dir_path}/input/day05.txt'

    with open(filepath) as f:
        lines = f.read().strip().split('\n\n')

        seeds_line = lines[0].strip().split(': ')[1]
        seeds = list(map(int, seeds_line.split()))

        source_to_dest_maps = []
        for from_to_map in lines[1:]:
            map_definition = (from_to_map.split('map:\n')[1]).split('\n')
            map_rules = list(map(lambda x: dict_key_value(*(x.split())), map_definition))
            map_dict = dict((rule_range, change) for rule_range, change in map_rules)
            source_to_dest_maps.append(map_dict)

        locations = list(map(lambda seed: calculate_from_maps(seed, source_to_dest_maps), seeds))

        print('Part 1: ')
        print(min(locations))

        new_seeds = [seed_range(seeds[i: i + 2]) for i in range(0, len(seeds), 2)]
        dest_to_source_maps = list(map(lambda x: dest_to_source_map(x), reversed(source_to_dest_maps)))

        for location in range(0, 100000000):
            seed = calculate_from_maps(location, dest_to_source_maps)
            if any(low <= seed <= high for (low, high) in new_seeds):
                print('Part 2:')
                print(location)
                return


if __name__ == '__main__':
    main()
