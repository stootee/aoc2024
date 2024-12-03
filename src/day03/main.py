from utils import get_input
import part1
import part2

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

def run(input_file='input.txt'):
    input = "".join(get_input(input_file))

    part1.run(input=input)

    part2.run(input=input)

if __name__ == '__main__':
    run()