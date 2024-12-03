from utils import get_input
import part1
import part2

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def run(input_file='input.txt'):
    input = get_input(input_file)

    processed_input = []
    for row in input:
        processed_input.append(list(map(int, row.split())))

    part1.run(input=processed_input)

    part2.run(input=processed_input)

if __name__ == '__main__':
    run()