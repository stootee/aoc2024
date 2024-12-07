from utils import timing
from itertools import product

@timing
def run(*args, **kwargs):
    input = kwargs.get('input')
    operators = ['*', '+']

    valid = []

    for k, v in input.items():
        operator_combinations = product(operators, repeat=len(v) - 1)

        for combo in operator_combinations:
            evaluate = int(v[0])
            for n, op in enumerate(combo):
                c = f"{evaluate} {op} {v[n + 1]}"

                evaluate = eval(c)

            if evaluate == int(k):
                calculation = ''.join(num + op for num, op in zip(v, combo)) + v[-1]
                # print(f"{calculation} = {k}")
                valid.append((k, calculation))
                break
    
    print("Part1:", sum([int(ans) for ans, calc in valid]))
