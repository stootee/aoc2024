from utils import timing
import re

def find_keyword(pos):
    kw_found = False
    if text[pos:4] == "do()":
        DO = True
        pos += 4
        kw_found = True
    elif text[pos:7] == "don't()":
        DO = False
        pos += 7
        kw_found = True
    
    return kw_found

@timing
def run(*args, **kwargs):
    # Input string
    text = kwargs['input']
    text = "do()" + text

    # Regex pattern to match the keywords
    pattern = r"do\(\)|don't\(\)"

    # Find all matches and their positions
    matches = list(re.finditer(pattern, text))

    # Prepare the result list
    result = []

    # Track the end position of the previous match
    start = 0

    for match in matches:
        # Extract the matched keyword
        keyword = match.group()
        
        # Extract the substring starting from the end of the match to the start of the next match
        if start != 0:
            value = text[start:match.start()]
            result.append((prev_keyword, value))

        # Update the start position and save the current keyword
        start = match.end()
        prev_keyword = keyword

    # Add the final part after the last keyword
    if start < len(text):
        result.append((prev_keyword, text[start:]))

    results = 0
    for x, y in result:
        if x == "do()":

            # Regex to extract the patterns
            pattern = r"mul\((\d+),(\d+)\)"

            # Find all matches
            matches = re.findall(pattern, y)

            for a, b in matches:
                results += int(a) * int(b)

    print("Part2:", results)