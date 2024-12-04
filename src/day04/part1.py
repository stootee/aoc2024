from utils import timing

def word_search(x_coord, y_coord, pattern):
    directions = {
        'e': (1, 0),
        'se': (1, 1), 
        's': (0, 1), 
        'sw': (-1, 1), 
        'w': (-1, 0), 
        'nw': (-1, -1), 
        'n': (0, -1), 
        'ne': (1, -1)
        }

    look_here = []
    for direction, xy in directions.items():
        x_dir, y_dir = xy
        lh = []
        for s in range(len(pattern)):
            lh.append(((x_coord + (x_dir * s)), (y_coord + (y_dir * s))))
        yield (direction, lh)


@timing
def run(*args, **kwargs):

    input = kwargs['input']

    pattern = 'XMAS'

    patterns_found = 0

    for y, r in enumerate(input):
        for x, c in enumerate(r):

            if c == pattern[0]:
                search_coords = word_search(x, y, pattern)

                for dirname, direction in search_coords:
                    found_word = ""
                    print('\n', dirname, direction, '', end='')
                    for look_x, look_y in direction:
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
                
            else:
                # not a starting point
                pass
    print("Part1:", patterns_found)
