import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import get_input
import part1
import part2

def run(input_file='input.txt'):
    input = get_input(input_file)

    page_rules = {}
    updates = []
    raw_pr = []
    
    for row in input:
        if '|' in row:
            raw_pr.append(row)
            try:
                page_rules[row.split('|')[0]].append(row.split('|')[1])
            except:
                page_rules[row.split('|')[0]] = [row.split('|')[1]]

        elif "," in row:
            updates.append(row.split(','))

    # part1.run(page_rules=page_rules, updates=updates)

    part2.run(page_rules=page_rules, raw_pr=raw_pr, updates=updates)

if __name__ == '__main__':
    run()