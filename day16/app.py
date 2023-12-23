import os
import matplotlib.pyplot as plt

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp

GRID = []
PATHS = []
LINKS = {
    "N": {"\\": "W", "|": "N", "/": "E", "-": ("E", "W")}, 
    "E": {"\\": "S", "|": ("N", "S"), "/": "N", "-": "E"},
    "S": {"\\": "E", "|": "S", "/": "W", "-": ("E", "W")},
    "W": {"\\": "N", "|": ("N", "S"), "/": "S", "-": "W"},
}
BEAMS = []


class Beam:
    visited = []
    direction = None
    coordinates = None
    moving = True

    def __init__(self, start=(0, 0), direction='E'):
        self.coordinates = start
        self.direction = direction
        self.turn()


    def split(self, direction):
        for d in direction:
            BEAMS.append(Beam(self.coordinates, d))

    
    def turn(self):
        if self.moving:
            surface = GRID[self.coordinates[1]][self.coordinates[0]]
            
            try:
                self.direction = LINKS[self.direction][surface]
                # print(surface, self.direction)
                if len(self.direction) == 2:
                    self.moving = False
                    self.split(self.direction)
                    # print('beam splits')

            except:
                pass


    def move(self):
        directions = {
            "N": (0, -1), 
            "E": (1, 0),
            "S": (0, 1),
            "W": (-1, 0)
        }

        if self.moving:
            new_position = tuple(map(sum, zip(self.coordinates, directions[self.direction])))

            if new_position[0] >= 0 and new_position[0] < len(GRID[0]) and new_position[1] >= 0 and new_position[1] < len(GRID):
                self.coordinates = new_position
                self.turn()
                pos = (new_position, self.direction)
                if not pos in PATHS:
                    PATHS.append(pos)
                else:
                    # print('we''ve been here before', pos)
                    self.moving = False
            else:
                self.moving = False
                # print('beam off the grid')

            
for r in get_input('input'):
    GRID.append([x for x in r])


def get_path(start, direction):
    cnt = 0
    BEAMS.clear()
    BEAMS.append(Beam(start, direction))
    moving = True
    PATHS.clear()
    energised = set()
    while moving:

        for b in BEAMS:
            if b.moving:
                energised.add(b.coordinates)
                b.move()

        moving = [1 for b in BEAMS if b.moving]
        cnt += 1

        if cnt % 1000 == 0:
            print(cnt, len(BEAMS), len(moving), len(energised))

    return energised
        
energised = get_path(start=(0, 0), direction='E')

print("Part1:", len(energised))

def plot_the_path(path):
    plt.scatter([x[0] for x in path], [x[1] for x in path], marker='o', color='red', label='Energised')
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.xlim([-1, len(GRID[0])])
    plt.ylim([len(GRID), -1])
    plt.show()

# plot_the_path(energised)


best_point = ((None, None), '', set())
for start_direction in ['S', 'N', 'W', 'E']:
    for insert_point in range(max([len(GRID), len(GRID[0])])):
        if start_direction in ['S']:
            start_x = insert_point
            start_y = 0
        elif start_direction in ['E']:
            start_y = insert_point
            start_x = 0
        elif start_direction in ['W']:
            start_y = insert_point
            start_x = len(GRID[0]) -1
        elif start_direction in ['N']:
            start_x = insert_point
            start_y = len(GRID) -1
            
        else:
            print('i got here')


        # print(start_x, start_y, start_direction)
        path = get_path((start_x, start_y), start_direction)

        # plot_the_path(path)

        if len(path) > len(best_point[2]):
            best_point = ((start_x, start_y), start_direction, path)

print(best_point[0], best_point[1], len(best_point[2]))
plot_the_path(best_point[2])