from utils import timing

@timing
def run(*args, **kwargs):

    obstacles = set(kwargs.get('obstacles'))
    guard_pos1, guard_direction1 = kwargs.get('guard')
    boundary = kwargs.get('boundary')
    DIRECTION = kwargs.get('direction')

    # obstacles = [(4, 0), (9, 1), (2, 3), (7, 4), (1, 6), (8, 7), (0, 8), (6, 9)]
    # guard_pos1 = (4, 6)
    # guard_direction1 = [(0, -1), '>']
    # boundary = (10, 10)
    # DIRECTION = {'<': [(-1, 0), '^'], '^': [(0, -1), '>'], '>': [(1, 0), 'V'], 'V': [(0, 1), '<']}

    blocker = set()

    for y in range(boundary[0]):

        for x in range(boundary[1]):
            # print((x, y), '   ', end='\r')
            visited = set()
            guard_pos = guard_pos1
            guard_direction = guard_direction1.copy()

            obstacles2 = obstacles.copy()
            if not (x, y) == guard_pos:
                obstacles2.add((x, y))

            while guard_pos[0] <= boundary[0] and guard_pos[1] <= boundary[1] and guard_pos[0] >= 0 and guard_pos[1] >= 0:
                visited.add((guard_pos, guard_direction[0]))

                new_guard_pos = (guard_pos[0] + guard_direction[0][0], guard_pos[1] + guard_direction[0][1])

                if new_guard_pos in obstacles2:
                    guard_direction = DIRECTION[guard_direction[1]]
                else:
                    guard_pos = new_guard_pos

                if (guard_pos, guard_direction[0]) in visited:
                    blocker.add((x, y))
                    break
    
    print("Part2:", len(blocker))
