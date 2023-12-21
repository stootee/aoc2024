import os
import numpy

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp


def rotate(plate):
    return numpy.rot90(plate)


p = get_input('input')
p = list(zip(*p))

CYCLES = []
cycle_weights = []
cntr = 0
while cntr < 1000000000:
    cycle = []

    for c in range(4):

        cols = []
        for x in p:
            x = list(x)
            start = 0
            end = len(x)
            l = []
            found = 0
            for n, y in enumerate(x):
                if y == '#':
                    l.append(x[found:n])
                    found = n
            l.append(x[found:])

            n = []
            for m in l:
                while True:
                    o = list(m)
                    for y in range(len(m)):
                        if m[y] == '.':
                            m.pop(y)
                            m.append('.')
                    if m == o:
                        n.append(m)
                        break

            cols.append([j for i in n for j in i])
        p = list(cols)
        p = rotate(p)

    cycle = ""
    for x in rotate(p)[::-1]:
        cycle += "".join(x) + '\n'

    weight = 0
    for col in p:
        l = len(col)
        for cn, b in enumerate(col):
            if b == 'O':
                weight += l - cn

    
    if not cycle in CYCLES:
        cycle_weights.append(('cycle:', cntr, 'weight:', weight))
        CYCLES.append(cycle)
        cntr += 1

    else:
        ci = CYCLES.index(cycle)
        print('Cycle Found at', ci)
        break


for c, x in enumerate(cycle_weights):
    cntr += 1
    print(c, cntr, x)


print('cycles completed: ', len(cycle_weights))
print('cycle loop length:', len(cycle_weights[ci:]))
done = 1000000000 - len(cycle_weights)
print('cycles remaining: ', done)

complete_loops = done // len(cycle_weights[ci:])
print('complete_loops:   ', complete_loops)

remaining_cycles = 1000000000 - (complete_loops * len(cycle_weights[ci:])) - len(cycle_weights)
print('remaining cycles: ', remaining_cycles)
print(cycle_weights[ci:][remaining_cycles])
