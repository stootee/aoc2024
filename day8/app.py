import os
from operator import add 
from math import gcd

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp

i = get_input('input')

instructions = i[0]

POINTS = {}
for point in i[2:]:
    POINTS[point[0:3]] = {'L': point[7:10], 'R': point[12:15]}


class Ghost:
    this_point = None

    def __init__(self, this_point):
        self.this_point = this_point

    def where_am_i(self):
        return self.this_point[-1]
    
    def make_a_move(self, move):
        self.this_point = POINTS[self.this_point][move]
    
if 'AAA' in POINTS:
    ghost1 = Ghost('AAA')
    counter = 0
    while not ghost1.this_point == 'ZZZ':
        for instruction in instructions:
            ghost1.make_a_move(instruction)
            counter += 1

    print("part1:", counter)

ghosts = []
for point in POINTS:
    if point[-1] == 'A':
        ghosts.append(Ghost(point))


# part2
# find the number of steps to the first z

start_points = []
for point in POINTS:
    if point[-1] == 'A':
        start_points.append(Ghost(point))


paths = []
for ghost in ghosts:

    first_zed = None
    counter = 0
    found_a_zed = False
    while True:
        for instruction in instructions:
            ghost.make_a_move(instruction)
            counter += 1

            if ghost.where_am_i() == 'Z':
                found_a_zed = True

        if found_a_zed:
            if not first_zed:
                first_zed = ghost.this_point
                count_to_first_zed = counter
                counter = 0
            elif ghost.this_point == first_zed:
                count_to_return_zed = counter
                break
                
    if count_to_first_zed == count_to_return_zed:
        paths.append(count_to_first_zed)

print(paths)

lcm = paths.pop()

for path in paths:
    lcm = lcm * path // gcd(lcm, path)

print('part2:', lcm)
