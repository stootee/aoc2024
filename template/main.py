import sys
import os
import datetime

current_directory = os.path.dirname(os.path.realpath(__file__))

def get_input(input_file=f'{current_directory}/input.txt') -> list: 
    with open(input_file) as input:
        i =  input.read().splitlines()

    return i

def run(input=get_input()):
    pass
    # for row in input:
    #     print(row)


if __name__ == '__main__':
    run()