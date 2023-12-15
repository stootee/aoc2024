import os
from operator import add 

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp


def find_pattern(seq, forward=True):
    r = []
    if not forward:
        seq.reverse()
    
    for x in range(len(seq) - 1):
        this_sum = int(seq[x + 1]) - int(seq[x])
        r.append(this_sum)

    

    if set(r) == {0}:
        return 0
    else:
        num = find_pattern(r) + r[-1]
        return num

part1 = 0
part2 = 0
for sequence in get_input('input'):
    sequence = sequence.split(" ")
    part1 += find_pattern(sequence) + int(sequence[-1])
    part2 += find_pattern(sequence, False) + int(sequence[-1])

print("part1:", part1)
print("part2:", part2)
    
