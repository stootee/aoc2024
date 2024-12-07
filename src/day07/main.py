import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import get_input
import part1
import part2

def run(input_file='input.txt'):
    input = get_input(input_file)

    processed_input = {}

    for x in input:
        answer, numbers = x.split(":")
        numbers = numbers.strip().split(" ")

        processed_input[answer] = numbers

    print("Uniqueness Check:", len(processed_input) == len(input))

    part1.run(input=processed_input.copy())

    part2.run(input=processed_input.copy())

if __name__ == '__main__':
    run('input.txt')