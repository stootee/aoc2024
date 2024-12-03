from utils import timing
import re

@timing
def run(*args, **kwargs):
    # Input string
    text = kwargs['input']

    # Regex to extract the patterns
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all matches
    matches = re.findall(pattern, text)

    results = 0
    for a, b in matches:
        results += int(a) * int(b)

    print("Part1:", results)
