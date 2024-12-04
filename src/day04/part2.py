from utils import timing

def word_search(x_coord, y_coord, pattern):
    directions = {
        'x1': [(-1, -1), (0, 0), (1, 1)],
        'x2': [(1, 1), (0, 0), (-1, -1)],
        'x3': [(-1, 1), (0, 0), (1, -1)],
        'x4': [(1, -1), (0, 0), (-1, 1)],
        }

    for direction, xy in directions.items():
        x_dir, y_dir = xy
        lh = []
        for s in directions:
            lh.append(((x_coord + (x_dir * s)), (y_coord + (y_dir * s))))
        yield (direction, lh)


@timing
def run(*args, **kwargs):

    input = kwargs['input']

    pattern = 'MAS'

    patterns_found = 0
    x_found = 0

    directions = {
        'x1': [(-1, -1), (0, 0), (1, 1)],
        'x2': [(1, 1), (0, 0), (-1, -1)],
        'x3': [(-1, 1), (0, 0), (1, -1)],
        'x4': [(1, -1), (0, 0), (-1, 1)],
        }

    for y, r in enumerate(input):
        for x, c in enumerate(r):
            patterns_found = 0

            if c == pattern[1]:

                for dirname, direction in directions.items():
                    found_word = ""

                    print('\n', dirname, direction, '', end='')
                    for lx, ly in direction:
                        look_x = x + lx
                        look_y = y + ly
                        try:
                            if look_x < 0 or look_y < 0:
                                raise Exception
                            letter = input[look_y][look_x]
                            found_word += letter
                            print(letter, end='')
                        except:
                            print(' bump!', (look_x, look_y), end='')
                            break
                    
                    if found_word == pattern:
                        patterns_found += 1
                        print(' found! ', end='')
                
                if patterns_found > 1:
                    x_found += 1
                
            else:
                # not a starting point
                pass
    print("\nPart2:", x_found)
