from aoc import get_input
from functools import cmp_to_key

data = get_input(7).splitlines()
order_of_cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

cards = []
for line in data:
    card, bid = line.split()
    cards.append((card, bid))

def compare(card1, card2):
    if card1 == card2:
        return 0
    else:
        card1_type = get_card_type(card1)
        card2_type = get_card_type(card2)

        if card1_type > card2_type:
            return -1
        elif card1_type < card2_type:
            return 1
        else:
            for char1, char2 in zip(card1, card2):
                if order_of_cards.index(char1) < order_of_cards.index(char2):
                    return -1
                elif order_of_cards.index(char1) > order_of_cards.index(char2):
                    return 1

def get_card_type(card):
    card_dict = {}
    if card == 'JJJJJ':
        return 6

    for char in card:
        card_dict[char] = card_dict.get(char, 0) + 1

    items_ = [(k,v) for k,v in card_dict.items()] 
    items_ = sorted(items_, key=lambda item: item[1], reverse=True)
    
    for key, _ in items_:
        if key != 'J':
            key_max = key
            break
    for char in card:
        if char == 'J':
            card_dict[key_max] += 1
    if 'J' in card_dict:
        del card_dict['J']
    
    values = sorted(card_dict.values(), reverse=True)
    
    if len(values) == 1:
        # 5 of a kind
        return 6
    elif len(values) == 2 and 4 in values:
        # 4 of a kind
        return 5
    elif len(values) == 2 and 3 in values:
        # Full house
        return 4
    elif len(values) == 3 and 3 in values:
        # 3 of a kind
        return 3
    elif len(values) == 3 and 2 in values:
        # two pair
        return 2
    elif len(values) == 4:
        # one pair
        return 1
    else:
        # high card
        return 0
    
cards = sorted(cards, key=cmp_to_key(lambda item1, item2: compare(item1[0], item2[0])))

sum_of_bids = 0
cards_len = len(cards)
for i, card in enumerate(cards):
    # print(card, cards_len - i) 
    sum_of_bids += int(card[1]) * (cards_len - i)

print(sum_of_bids)