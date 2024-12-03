from utils import timing

@timing
def run(*args, **kwargs):
    
    safe_rows = 0
    for row in kwargs['input']:
        print(row)
        safe = True
        first_to_last = row[0] - row[-1]

        if first_to_last == 0:
            print('not ascending or descending')
            safe = False
            continue

        for x in range(len(row) - 1):
            neighbour_diff = row[x] - row[x + 1]

            if abs(neighbour_diff) < 1 or abs(neighbour_diff) > 3:
                print('not slow enough')
                safe = False
                break

            if first_to_last < 0 and neighbour_diff > 0:
                print('shouldn''t increase when overall is decreasing')
                safe = False
                break

            if first_to_last > 0 and neighbour_diff < 0:
                print('shouldn''t decrease when overall is increasing')
                safe = False
                break

        if safe: 
            print('safe')
            safe_rows += 1
    print("Part1:", safe_rows)
