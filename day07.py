import os
import functools

dir_path = os.path.dirname(os.path.realpath(__file__))


hand_strengths = {'FIVE': 1, 'FOUR': 2, 'FULL_HOUSE': 3, 'THREE': 4, 'TWO_PAIRS': 5, 'PAIR': 6, 'HIGH_CARD': 7}
card_strengths_1 = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}
card_strengths_2 = card_strengths_1.copy()
card_strengths_2['J'] = 14


def parse_card(line):
    parts = line.split()
    return parts[0], int(parts[1])


def hand(card):
    scores_dict = {x: card.count(x) for x in card}
    scores = list(scores_dict.values())
    if 5 in scores:
        return hand_strengths['FIVE']
    elif 4 in scores:
        return hand_strengths['FOUR']
    elif 3 in scores and 2 in scores:
        return hand_strengths['FULL_HOUSE']
    elif 3 in scores:
        return hand_strengths['THREE']
    elif scores.count(2) == 2:
        return hand_strengths['TWO_PAIRS']
    elif 2 in scores:
        return hand_strengths['PAIR']
    else:
        return hand_strengths['HIGH_CARD']


def compare_cards_in_order(card1, card2, strengths=card_strengths_1):
    for i in range(len(card1)):
        if strengths[card1[i]] > strengths[card2[i]]:
            return 1
        elif strengths[card1[i]] < strengths[card2[i]]:
            return -1
    return 0


def compare(card1, card2):
    hand1 = hand(card1[0])
    hand2 = hand(card2[0])
    if hand1 > hand2:
        return 1
    elif hand1 < hand2:
        return -1
    else:
        return compare_cards_in_order(card1[0], card2[0])


def main():
    filepath = f'{dir_path}/input/day07.txt'

    with open(filepath) as f:
        cards = list(map(lambda x: parse_card(x), f.read().strip().split('\n')))

    sorted_cards = sorted(cards, key=functools.cmp_to_key(compare))

    rank = len(sorted_cards)
    total_winnings = 0
    for card in sorted_cards:
        total_winnings += rank * card[1]
        rank -= 1

    print('Part 1:')
    print(total_winnings)


if __name__ == '__main__':
    main()
