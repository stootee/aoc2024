import os
import re

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp

def hash_value(string='HASH'):
    hv = 0
    for x in string:
        hv += ord(x)
        hv *= 17

    return hv - ((hv // 256) * 256)


summary = 0
for s in get_input('input')[0].split(','):
    summary += hash_value(s)

print("part1:", summary)

boxes = {}
for s in get_input('input')[0].split(','):

    search_position = re.search(r'[=-]', s).start()

    label = s[:search_position]
    box_no = hash_value(label)

    idx = None
    idx_found = False
    try:
        idx = list(zip(*boxes[box_no]))[0].index(label)
        idx_found = True
    except Exception as ex:
        pass
    
    if '=' in s:
        focal_length = s[search_position + 1:]
        try:
            if idx_found:
                boxes[box_no].pop(idx)
                boxes[box_no].insert(idx, (label, focal_length))
            else:
                boxes[box_no].append((label, focal_length))
        except KeyError as ex:
            boxes[box_no] = [(label, focal_length)]
    elif idx_found:
        boxes[box_no].pop(idx)
    else:
        pass

focusing_power = 0
for box, lenses in boxes.items():
    for slot, lens in enumerate(lenses):
        label, focal_length = lens
        focusing_power += int((box + 1)) * int((slot + 1)) * int(focal_length)

print('part2:', focusing_power)
