import datetime

with open('/Users/stu/Projects/aoc2023/day4/input.txt') as inp:
    i = inp.read().splitlines()


def card_score(numbers):
    if numbers:
        return 2**(len(numbers)-1)
    else:
        return 0


cards = {}
score = 0
for x in i:

    card, numbers = x.split(':')
    winning_numbers, card_numbers = numbers.split('|')
    winning_numbers = set(winning_numbers.split())
    card_numbers = set(card_numbers.split())

    score += card_score(card_numbers.intersection(winning_numbers))

    cards[int(card[5:8])] = {'card_ numbers': card_numbers, 'winning_numbers': winning_numbers, 'winning_numbers_number': len(card_numbers.intersection(winning_numbers)), 'score': score, 'count': 1}

print(datetime.datetime.now())
print('part1', score)  


ultimate_scratch = 0
for card in range(1, len(cards) + 1):
    details = cards[card]
    for win in range(details['winning_numbers_number']):
        for num in range(details['count']):
            cards[card + win + 1]['count'] += 1
    
    ultimate_scratch += cards[card]['count']

print('part2', ultimate_scratch)
print(datetime.datetime.now())