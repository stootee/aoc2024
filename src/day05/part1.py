from utils import timing

@timing
def run(*args, **kwargs):
    page_rules = kwargs['page_rules']

    correct_updates = []
    middles = 0
    for update in kwargs['updates']:
        correct = True
        for n, page in enumerate(update):
            if not set(update[n + 1:]).issubset(set(page_rules.get(page, []))):
                correct = False
                break
        
        if correct:
            correct_updates.append(update)
            middles += int(update[int((len(update) - 1) / 2)])

    print("Part1:", middles)
