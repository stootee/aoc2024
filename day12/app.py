import os
from functools import reduce
from itertools import combinations
import re

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp

SPRINGS = {}
for id, row in enumerate(get_input('input')):
    mask, condition = row.split()
    condition = condition.split(',')
    SPRINGS[id] = {'mask': mask, 'condition': condition}


def assign(v, p):
  v[p[0]] = p[1]
  return v


def interp(word, letter, size):
  return ((reduce(assign, zip(comb, word), [letter] * size))
          for comb in combinations(range(size), len(word)))


def solve(unfold=1):
    possible_arrangements = 0

    for id in SPRINGS:
        # print(SPRINGS[id]['mask'])
        # print(SPRINGS[id]['condition'])
        mask = "?".join([SPRINGS[id]['mask']] * unfold)
        condition = SPRINGS[id]['condition'] * unfold
        # print(mask, condition)
        spring_set = ['#' * int(n) for n in condition]
        re_mask = mask.replace(".", "\.").replace("?", '.')
        pattern = re.compile(re_mask)
        # print(mask, condition, spring_set, re_mask)

        for x in interp(spring_set, '.', (len(mask) - len("".join(spring_set))) + len(spring_set)):
            st = "".join(x)
            new_ss = [x for x in st.split(".") if not x == '']

            if pattern.match(st):
                if spring_set == new_ss:
                    possible_arrangements += 1
                    # print(st)

    return possible_arrangements          

print("Part1:", solve(1))

# print("Part2:", solve(5))




