from utils import timing

def check_row(row):
    safe = False
    first_to_last = row[0] - row[-1]

    if first_to_last == 0:
        print('not ascending or descending')
        return safe, 0
        
    for x in range(len(row) - 1):
        neighbour_diff = row[x] - row[x + 1]

        if abs(neighbour_diff) < 1 or abs(neighbour_diff) > 3:
            print('not slow enough')
            return False, x

        if first_to_last < 0 and neighbour_diff > 0:
            print('shouldn''t increase when overall is decreasing')
            return False, x

        if first_to_last > 0 and neighbour_diff < 0:
            print('shouldn''t decrease when overall is increasing')
            return False, x
        
    return True, x


@timing
def run(*args, **kwargs):
    safe_rows = 0
    
    for row in kwargs['input']:
        print(row)
        safe, e = check_row(row)
        element_counter = len(row)

        while not safe and element_counter > 0:
            row_to_check = row.copy()

            row_to_check.pop(element_counter - 1)
            print("  ", row_to_check)

            safe, e = check_row(row_to_check)

            if not safe:
                element_counter -= 1


        if safe:
            print('safe')
            safe_rows += 1

    print("Part2:", safe_rows)
