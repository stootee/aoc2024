import os
from operator import add 

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp


numbers = []
markers = []

for y, row in enumerate(get_input('input')):
    part_no = ''
    these_coords = []
    print(row)
    for x, col in enumerate(row):

        if col.isnumeric():
            part_no += col
            these_coords.append((x, y))

        else:
            if part_no != '':
                numbers.append((part_no, these_coords))
                part_no = ''
                these_coords = []

            if not col == '.':
                markers.append((col, (x, y)))


    if part_no != '':
        numbers.append((part_no, these_coords))



def marker_perimeter(marker, coords):
    adjacents = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1)
    ]

    perimeter = []
    for adjacent_coords in adjacents:
        perimeter.append((tuple(map(add, coords, adjacent_coords))))

    return perimeter

marker_overlap = []
for marker, coords in markers:
    marker_overlap += marker_perimeter(marker, coords)

part_numbers = []
not_part_numbers = []
for partno, coord_list in numbers:
    found = False
    for x in coord_list:
        if x in marker_overlap:
            part_numbers.append(int(partno))
            found = True
            break
    if not found:
        not_part_numbers.append(int(partno))

# print(marker_overlap)
# print(numbers)


print('part1', sum(part_numbers))

# part 2

part2 = 0
print(marker_overlap)
for marker, coords in markers:
    # print(marker, coords)
    if marker == '*':
        partnos = []
        perimeter = set(marker_perimeter(marker, coords))
        for partno, mcoords in numbers:
            if len(set(mcoords).intersection(perimeter)) > 0:
                partnos.append(partno)
        
        if len(partnos) == 2:
            part2 += int(partnos[0]) * int(partnos[1])

        if len(partnos) > 2:
            print('more than 2!!!!')
            raise

print(part2)

            
