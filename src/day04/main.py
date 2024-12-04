import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import get_input
import part1
import part2

def run(input_file='input.txt'):
    input = get_input(input_file)

    part1.run(input=input)

    part2.run(input=input)

if __name__ == '__main__':
    run()