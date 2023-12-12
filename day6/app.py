import os
from operator import add
from math import prod

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def get_input(filename='input'):
    with open(f"{filename}.txt") as input:

        inp = input.read().splitlines()
    
    return inp


HANDS = {}
for x in get_input('input'):
    cards = []
    hand, bet = x.split(' ')
    for card in hand:
        cards.append(card)

    HANDS[hand] = {
        'cards': cards, 
        'bet': int(bet),
        }
    

def card_score(hand, joker=True):
        
    card_strength = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'J': 10,
        'T': 9,
        '9': 8,
        '8': 7,
        '7': 6,
        '6': 5,
        '5': 4,
        '4': 3,
        '3': 2,
        '2': 1,
    }

    if joker:
        card_strength['J'] = 0

    c_score = ()
    for c in hand:
        c_score += (card_strength[c],)

    return c_score + (hand,)


def card_counter(cards):
    card_count = {}

    for c in cards:
        try:
            card_count[c] += 1
        except KeyError:
            card_count[c] = 1

    return card_count


def hand_type(count):

    if len(count.values()) == 1:
        return 'Five of a kind', 7
    elif max(count.values()) == 4:
        return 'Four of a kind', 6
    elif len(count.values()) == 2:
        return 'Full House', 5
    elif max(count.values()) == 3:
        return 'Three of a kind', 4
    elif len(count.values()) == 3:
        return 'Two Pair', 3
    elif len(count.values()) == 4:
        return 'One Pair', 2
    elif len(count.values()) == 5:
        return 'High Card', 1
    else:
        return '????', 0
    
hand_scores = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}

for hand, details in HANDS.items():
    count = (card_counter(details['cards']))
    HANDS[hand]['count'] = count

    type, hand_strength = hand_type(count)
    HANDS[hand]['type'] = type
    HANDS[hand]['hand_strength'] = hand_strength

    cs = card_score(hand)
    hand_scores[hand_strength].append(cs)
    HANDS[hand]['card_score'] = cs


winnings = 0
rank = 0
for r in range(1, 8):
    for s in sorted(hand_scores[r]):
        rank += 1
        winnings += rank * HANDS[s[5]]['bet']

print("part1:", winnings)

def joker_test(hand):
    cards = HANDS[hand]['cards']
    best_score = 0
    print(hand)
    for t in ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1']:
        type, score = hand_type(card_counter(cards.replace('J', t)))
        print(t, type, score)


for h in HANDS:
    joker_test(h)