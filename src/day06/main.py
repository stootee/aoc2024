import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import get_input
import part1
import part2

def run(input_file='input.txt'):
    inp = get_input(input_file)

    obstacles = []
    guard = ()
    direction = {
        '<': [(-1, 0), '^'],
        '^': [(0, -1), '>'],
        '>': [(1, 0), 'V'],
        'V': [(0, 1), '<']
        }
    
    boundary = (len(inp), len(inp[0]))

    for y, row in enumerate(inp):
        for x, point in enumerate(row):
            if point == '#':
                obstacles.append((x, y))
            elif not point == '.':
                guard = ((x, y), direction[point])

    part1.run(obstacles=obstacles.copy(), guard=guard, boundary=boundary, direction=direction)

    part2.run(obstacles=obstacles.copy(), guard=guard, boundary=boundary, direction=direction)

if __name__ == '__main__':
    run()