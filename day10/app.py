import os
import matplotlib.pyplot as plt

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp

PIPE_MAP = []

LINKS = {
    "N": {"7": "W", "F": "E", "|": "N"}, 
    "E": {"J": "N", "7": "S", "-": "E"},
    "S": {"L": "E", "J": "W", "|": "S"},
    "W": {"L": "N", "F": "S", "-": "W"},
}

for y, row in enumerate(get_input('input')):
    pipe_row = []
    for x, pipe in enumerate(row):
        pipe_row.append(pipe)
        if pipe == 'S':
            start_point = (x, y)

    PIPE_MAP.append(pipe_row)


def navigate_pipe(point, direction=None):
    directions = {
        "N": (0, -1), 
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    x, y = point

    next_x = x + directions[direction][0]
    next_y = y + directions[direction][1]

    if next_x > len(PIPE_MAP[0]) or next_x < 0 or next_y > len(PIPE_MAP) or next_y < 0:
        # print("coordinate out of range")
        return None, None

    next_pipe = PIPE_MAP[next_y][next_x]

    if next_pipe == 'S':
        print('Back to the start')
        return (next_x, next_y), None
    
    elif not next_pipe in LINKS[direction]:
        # print("Not a valid move")
        return None, None
    
    else:
        return (next_x, next_y), LINKS[direction][next_pipe]
    

coordinates = [start_point]
start_directions = []
for start in ["N", "E", "S", "W"]:
    new_point, direction = navigate_pipe(start_point, start)
    if direction:
        start_directions.append((new_point, direction))


for new_point, direction in start_directions:
    counter = 1
    new_point, direction = start_directions[0]
    while not new_point == start_point:
        coordinates.append(new_point)
        new_point, direction = navigate_pipe(new_point, direction)
        counter += 1

    print(counter / 2)

# part 2
starters = {
    '7': [],
    'F': [],
    '|': [],
    '-': [],
    'J': [],
    'L': [],
}

for z in LINKS.values():
    for p, d in z.items():
        starters[p].append(d)

what_is_s = None
for a, b in starters.items():
    if start_directions[0][1] in b and start_directions[1][1] in b:
        what_is_s = a
        break


PIPE_MAP[start_point[1]][start_point[0]] = what_is_s

insiders = []
inside = -1
counter = 0
for y, row in enumerate(PIPE_MAP):
    for x, col in enumerate(row):
        for pipe in col:
            if (x, y) in coordinates:
                if pipe in ["|", "J", "L"]:
                    inside *= -1

            if inside > 0 and (x, y) not in coordinates:
                insiders.append((x, y))
                counter += 1


# Extract x and y coordinates separately
x_coords, y_coords = zip(*coordinates)

# Extract x and y coordinates separately
inside_x_coords, inside_y_coords = zip(*insiders)

print(counter)

# Plot the coordinates on a grid
plt.scatter(x_coords, y_coords, marker='.', color='red', label='Pipes')
plt.scatter(inside_x_coords, inside_y_coords, marker='.', color='blue', label='Inside')
plt.scatter(start_point[0], start_point[1], marker='o', color='green', label='Start')
plt.gca().invert_yaxis()
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()