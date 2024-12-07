from utils import timing
from itertools import product

def calculate(input, operators):
    valid = []
    invalid = {}

    for k, v in input.items():
        operator_combinations = product(operators, repeat=len(v) - 1)

        for combo in operator_combinations:
            evaluate = int(v[0])
            n = 0
            for op in combo:

                if op == '||':
                    c = f"{evaluate}{v[n + 1]}"
                else:
                    c = f"{evaluate} {op} {v[n + 1]}"

                evaluate = eval(c)
                n += 1

            if evaluate == int(k):
                calculation = ''.join(num + op for num, op in zip(v, combo)) + v[-1]
                # print(f"{calculation} = {k}")
                valid.append((k, calculation))
                break
            
            invalid[k] = v

    return valid, invalid

@timing
def run(*args, **kwargs):
    inp = kwargs.get('input')
    ops = ['*', '+', '||']

    v1, i1 = calculate(inp, ['*', '+'])
    v2, i2 = calculate(i1, ['*', '+', '||'])

    print("Part2:", sum([int(ans) for ans, calc in v1]) + sum([int(ans) for ans, calc in v2]))
