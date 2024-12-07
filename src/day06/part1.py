from utils import timing

@timing
def run(*args, **kwargs):

    obstacles = kwargs.get('obstacles')
    guard_pos, guard_direction = kwargs.get('guard')
    boundary = kwargs.get('boundary')
    DIRECTION = kwargs.get('direction')

    visited = [(guard_pos[0], guard_pos[1])]

    while guard_pos[0] <= boundary[0] and guard_pos[1] <= boundary[1] and guard_pos[0] >= 0 and guard_pos[1] >= 0:
        if not guard_pos in visited:
            visited.append(guard_pos)

        new_guard_pos = (guard_pos[0] + guard_direction[0][0], guard_pos[1] + guard_direction[0][1])

        if new_guard_pos in obstacles:
            guard_direction = DIRECTION[guard_direction[1]]
        else:
            guard_pos = new_guard_pos

    # for y in range(boundary[0]):
    #     for x in range(boundary[1]):
    #         if (x, y) in visited:
    #             print('X', end='')
    #         elif (x, y) in obstacles:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
        
    print("Part1:", len(visited))
