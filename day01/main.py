import sys
import os
import datetime
from part1 import part1
from part2 import part2

current_directory = os.path.dirname(os.path.realpath(__file__))

def get_input(input_file) -> list: 
    with open(f'{current_directory}/{input_file}') as input:
        i =  input.read().splitlines()

    return i


def format_input(input):
    list1 = []
    list2 = []
    for row in input:
        e1, e2 = row.split('   ')
        list1.append(int(e1))
        list2.append(int(e2))

    return list1, list2


def run(input_file='input.txt'):
    input = get_input(input_file)

    list1, list2 = format_input(input)

    list1.sort()
    list2.sort()

    part1(list1, list2)

    part2(list1, list2)


if __name__ == '__main__':
    run('input.txt')