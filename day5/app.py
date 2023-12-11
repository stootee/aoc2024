import os
from operator import add 

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp


MAPS = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': [],
    }

def mapper(my_map):
    child_start, parent_start, length = my_map.split(' ')
    parent_start = int(parent_start)
    child_start = int(child_start)
    length = int(length)
    
    return ((parent_start, parent_start + length), (child_start, child_start + length))


def map_values(value, map_type, reverse=False):
    value = int(value)
    for x in MAPS[map_type]:
        if reverse:
            if value in range(x[1][0], x[1][1]):
                position = value - x[1][0]

                return range(x[0][0], x[0][1])[position]

        else:
            if value in range(x[0][0], x[0][1]):
                position = value - x[0][0]

                return range(x[1][0], x[1][1])[position]
            
    return value

def to_the_end(val, reverse=False):
    k = MAPS.keys()
    if reverse:
        k = k.__reversed__()

    for x in k:
        val = map_values(val, x, reverse)

    return val

map_type = None

for x in get_input('input'):
    if 'seeds: ' in x:
        seeds = x[7:].split()

    if x == 'seed-to-soil map:':
        map_type = 'seed-to-soil'

    elif x == 'soil-to-fertilizer map:':
        map_type = 'soil-to-fertilizer'

    elif x == 'fertilizer-to-water map:':
        map_type = 'fertilizer-to-water'

    elif x == 'water-to-light map:':
        map_type = 'water-to-light'

    elif x == 'light-to-temperature map:':
        map_type = 'light-to-temperature'

    elif x == 'temperature-to-humidity map:':
        map_type = 'temperature-to-humidity'

    elif x == 'humidity-to-location map:':
        map_type = 'humidity-to-location'

    elif map_type and x:
        MAPS[map_type].append(mapper(x))


locations = []
for seed in seeds:
    locations.append(to_the_end(seed))

print('part1:', min(locations))

part2_seeds = []
s = 0
start_range = set()

for x in range(int(len(seeds) / 2)):

    part2_seeds.append(range(int(seeds[s]), int(seeds[s]) + int(seeds[s + 1])))
    start_range.add(int(seeds[s]))
    s += 2


for x in MAPS.values():
    for y in x:
        start_range.add(y[0][0])
        start_range.add(y[1][0])

loc = min(start_range)
cnt = 0

found = False
while not found:
    
    seed = to_the_end(loc, True)
    for s in part2_seeds:
        if seed in s:
            found = True
            break
    
    loc += 1
    if loc % 1000000 == 0:
        print(loc)

print('part2:', loc - 1)