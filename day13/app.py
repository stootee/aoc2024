import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def find_mirror(grid, smudges=0):

    for row in range(1, len(grid)):
        above = grid[:row][::-1]
        below = grid[row:]

        num_diff = 0
        for x, y in zip(above, below):
            for a, b in (zip(x, y)):
                if a != b:
                    num_diff += 1
        
        if num_diff == smudges:
            return row
    
    return 0
        

summary = 0


def get_result(file, smudges=0):
    summary = 0
    with open(f"{file}.txt") as input:

        for block in input.read().split('\n\n'):
            grid = block.splitlines()


            summary += find_mirror(grid, smudges) * 100
            summary += find_mirror(list(zip(*grid)), smudges)

    return summary


print('Part1:', get_result('test', 0))

print('Part2:', get_result('input', 1))







# PATTERNS = []
# counter = 0
# pattern = {'rows' : {}, 'cols': {}}
# cols = []
# for row in get_input('input'):
#     if row:
#         try:
#             pattern['rows'][row].append(counter)
#         except:
#             pattern['rows'][row] = [counter]

#         for c in range(len(row)):
#             if counter == 0:
#                 cols += [row[c]]
#             else:
#                 cols[c] += row[c]            

#         counter += 1

#     else:
#         for cnt, col in enumerate(cols):
#             try:
#                 pattern['cols'][col].append(cnt)
#             except:
#                 pattern['cols'][col] = [cnt]
#         PATTERNS.append(pattern)
#         pattern = {'rows' : {}, 'cols': {}}
#         counter = 0
#         cols = []

# for cnt, col in enumerate(cols):
#     try:
#         pattern['cols'][col].append(cnt)
#     except:
#         pattern['cols'][col] = [cnt]

# PATTERNS.append(pattern)

# summary = 0
# found = 0
# for c, p in enumerate(PATTERNS):
#     print(c)
#     for ln, multiplier in [('rows', 100), ('cols', 1)]:
#         matches = list(p[ln].values())
        
#         if len(matches[0]) == len(matches[-1]) == 1:
#             continue
#         for r in matches:
#             if len(r) >= 2 and 1 in [j-i for i, j in zip(r[:-1], r[1:])]:  
#                 line_count = max(r) * multiplier
#                 summary += line_count
#                 found += 1
#                 print(ln, matches)
#                 break

# print(summary, found)



    
