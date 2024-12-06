from utils import timing
from collections import defaultdict, deque

def build_graph(rules):
    # Build a graph where each node points to a list of pages that must come after it
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Parse each rule and add to the graph
    for rule in rules:
        before, after = map(int, rule.split('|'))
        graph[before].append(after)
        in_degree[after] += 1
        if before not in in_degree:
            in_degree[before] = 0
    
    return graph, in_degree

@timing
def run(*args, **kwargs):
    page_rules = kwargs['page_rules']
    raw_pr = kwargs['raw_pr']

    print(raw_pr)

    graph, in_degree = build_graph(raw_pr)

    print(in_degree)
    for k, v in in_degree.items():
        print(k, v)

    for k, v in graph.items():
        print(k, v)


    # Sorting the dictionary by its values (values are the same, so this is a simple sort of keys)
    sorted_data = sorted(prs_raw.items(), key=lambda x: x[1])
    print(sorted_data)

    # Output the result as a list of keys in sorted order
    prs = [str(key) for key, value in sorted_data]

    print(prs)

    correct_updates = []
    incorrect_updates = []
    middles = 0
    for update in kwargs['updates']:
        correct = True
        for n, page in enumerate(update):
            if not set(update[n + 1:]).issubset(set(page_rules.get(page, []))):
                correct = False
                incorrect_updates.append(update)
                break
        
        if correct:
            correct_updates.append(update)

    for update in incorrect_updates:

        corrected = []
        for u in update:
            # print('', u, page_rules.get(u, []))
            corrected.append((prs.index(u), u))

        corrected = sorted(corrected)
        corrected = [y for x, y in corrected]

        # print(f'{update}\n{corrected}')

        middles += int(corrected[int((len(corrected) - 1) / 2)])

    print("Part2:", middles)
