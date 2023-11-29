__author__ = '8175858, Braun'
import random
# my own error for exception handling


class MyError(Exception):
    pass


def create_card_list(number_of_cards: int) -> [(int, str)]:  # type: ignore
    '''
    creates a list of cards with the given number of cards by randomly choosing out of all available cards
    '''
    if number_of_cards > 32:
        raise MyError('Error create_card_list: too many cards')
    if number_of_cards < 0:
        raise MyError('Error create_card_list: too few cards')
    colors = ('Pik', 'Kreuz', 'Herz', 'Karo')
    all_cards = [(i, j) for i in range(1, 9) for j in colors]
    return random.sample(all_cards, number_of_cards)


def create_card_list2(number_of_cards: int) -> [(int, str)]:  # type: ignore
    """
    creates a list of tuple's (cards), with the colors green, red, yellow, blue (in german) and of the range 1 to
    number_of_cards.

    :param number_of_cards: number card of each type of cards
    :return: [(int, str)] - list of all the card for a game, len of the list is number_of_cards * 4
    """
    list_cards = []
    for i in range(1, number_of_cards + 1):
        for j in ["Kreuz", "Herz", "Karo"]:
            list_cards.append((i, j))
    return list_cards


def shuffle_card_list(cards: [(int, str)]) -> [(int, str)]:  # type: ignore
    '''
    shuffles the given list of cards with sorted() and random.random()
    '''
    return sorted(cards, key=lambda x: random.random())


def compare_two_cards(card_one: (int, str), card_two: (int, str)) -> int:  # type: ignore
    '''
    compares two cards and returns 0 if the first card is smaller, 1 if they are equal and 2 if the first card is bigger
    '''
    if card_one[0] < card_two[0]:
        return 0
    elif card_one[0] == card_two[0]:
        return 1
    else:
        return 2


def compare_two_cards_trump(card_one: (int, str), card_two: (int, str), trump: str) -> int:  # type: ignore
    '''
    compares two cards and returns 2 if the first card is trump and the second card is not, 0 if the first card is not trump and the second card is and the result of compare_two_cards() if both cards are trump or not trump
    '''
    if card_one[1] == trump and card_two[1] != trump:
        return 2
    elif card_one[1] != trump and card_two[1] == trump:
        return 0
    else:
        return compare_two_cards(card_one, card_two)


def hand_out_cards_old(list_cards: [(int, str)], players: int, number_of_cards: int) -> [[(int, str)]]:
    '''
    hands out equal number of cards to the given number of players
    each player gets one card handed out at a time
    raises an exception if there are not enough cards in the list
    '''
    if players * number_of_cards > len(list_cards):
        raise MyError('not enough cards')
    player_list = [[] for _ in range(players)]

    for _ in range(number_of_cards):
        for player in player_list:
            if not list_cards:
                break
            player.append(list_cards.pop())
    return player_list


def hand_out_cards(list_cards, players, number_of_cards):
    '''
    hands out equal number of cards to the given number of players
    each player gets one card handed out at a time
    raises an exception if there are not enough cards in the list
    '''
    if len(players) * number_of_cards > len(list_cards):
        raise MyError('not enough cards')
    player_list = {f'{players[i]}': []
                   for i in range(0, len(players))}

    for _ in range(number_of_cards):
        for player_cards in player_list.values():
            if not list_cards:
                break
            player_cards.append(list_cards.pop())
    return player_list


def main():
    card_list1 = create_card_list(4)
    card_list2 = create_card_list(2)
    card_list3 = create_card_list(8)
    try:
        print('create_card_list:')
        print(card_list1)
        print(card_list2)
        print(card_list3)
        print(create_card_list(33))
    except MyError as e:
        print(e)
    try:
        print('shuffle_card_list:')
        print(shuffle_card_list(card_list1))
        print(shuffle_card_list(card_list2))
        print(shuffle_card_list(card_list3))
    except MyError as e:
        print(e)

    print('compare_two_cards:')
    print(compare_two_cards((1, 'Pik'), (2, 'Pik')))
    print(compare_two_cards((1, 'Pik'), (1, 'Pik')))
    print(compare_two_cards((2, 'Pik'), (1, 'Pik')))

    print('compare_two_cards_trump:')
    print(compare_two_cards_trump((1, 'Pik'), (2, 'Pik'), 'Pik'))
    print(compare_two_cards_trump((1, 'Pik'), (1, 'Pik'), 'Pik'))
    print(compare_two_cards_trump((3, 'Pik'), (2, 'Pik'), 'Karo'))

    try:
        print('hand_out_cards:')
        print(hand_out_cards_old(card_list1, 2, 2))
        print(hand_out_cards_old(card_list2, 2, 1))
        print(hand_out_cards_old(card_list3, 4, 2))
    except MyError as e:
        print(e)


if __name__ == '__main__':
    main()
