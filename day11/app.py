import os
import copy
from itertools import combinations
import networkx as nx
from matplotlib import pyplot as plt

#doodledash
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp


def is_empty(arr):
    return "#" not in arr


def expand(arr):
    inserted = 0
    arr_copy = copy.deepcopy(arr)
    for cnt, r in enumerate(arr_copy):
        if is_empty(r):
            arr.insert(cnt + inserted + 1, r)
            inserted += 1

    return arr


def visualise_arr(arr):
    for x in arr:
        print("".join(x))


def transpose(arr):
    res = []
    for a_cnt, a in enumerate(arr):
        for item_cnt, item in enumerate(a):
            if a_cnt == 0:
                res.append([item])
            else:
                res[item_cnt].append(item)

    return res

def get_coords(arr, factor=2):
    coords = []
    rowcnt = 0
    colcnt = 0
    cols = transpose(arr)

    if not len(arr) == len(cols):
        raise

    for x in range(len(arr)):
        coords.append((rowcnt, colcnt))

        if is_empty(arr[x]):
            rowcnt += factor
        else:
            rowcnt += 1

        if is_empty(cols[x]):
            colcnt += factor
        else:
            colcnt += 1

    return coords


def get_results(this_arr, factor):
    expanded_map = get_coords(this_arr, factor)

    galaxies = []

    expanded_cols = [x[0] for x in expanded_map]
    expanded_rows = [x[1] for x in expanded_map]

    for y, yy in enumerate(this_arr):
        for x, xx in enumerate(yy):
            coords = (expanded_rows[x], expanded_cols[y])
            if xx == "#":
                galaxies.append(coords)

    path_length = 0
    for pair in combinations(galaxies, 2):
        pth = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

        path_length += pth

    return path_length

# read in the original map
o_map = []

for row in get_input('input'):
    row_arr = []
    for item in row:
        row_arr.append(item)
    o_map.append(row_arr)

print("part1:", get_results(o_map, 2))

print("part2:", get_results(o_map, 1000000))