import random


def create_card_list(number_of_cards: int) -> [(int, str)]:  # type: ignore
    colors = ('Pik', 'Kreuz', 'Herz', 'Karo')
    all_cards = [(i, j) for i in range(1, 8) for j in colors]
    return random.sample(all_cards, number_of_cards)


def shuffle_card_list(cards: [(int, str)]) -> [(int, str)]:  # type: ignore
    return sorted(cards, key=lambda x: random.random())


# type: ignore
# type: ignore
def compare_two_cards(card_one: (int, str), card_two: (int, str)) -> int:  # type: ignore
    if card_one[0] < card_two[0]:
        return 0
    elif card_one[0] == card_two[0]:
        return 1
    else:
        return 2


def compare_two_cards_trump(card_one: (int, str), card_two: (int, str), trump: str) -> int:  # type: ignore
    if card_one[1] == trump:
        return compare_two_cards(card_one, (card_one[0] + 1, trump))
    elif card_two[1] == trump:
        return compare_two_cards((card_two[0] + 1, trump), card_two)


def hand_out_cards(list_cards: [(int, str)], players: int, number_of_cards: int) -> [[(int, str)]]:  # type: ignore
    player_map = {f'player_{i}': [] for i in range(players)}
    for _ in range(number_of_cards):
        for player in player_map:
            if not list_cards:
                break
            player_map[player].append(list_cards.pop())
    return list(player_map.values())


if __name__ == '__main__':
    # print(create_card_list(4))
    # print(shuffle_card_list(create_card_list(32)))
    # print(compare_two_cards_trump((5, 'Herz'), (4, 'Herz')))
    print(hand_out_cards(shuffle_card_list(create_card_list(10)), 4, 5))
