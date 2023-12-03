"""
contains the functions for ERP04
"""

__author__ = "Matthias Kaschube"

import random


def create_card_list(number_of_cards: int) -> [(int, str)]:
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


def shuffle_card_list(cards: [(int, str)]) -> [(int, str)]:
    """
    Shuffle the card deck randomly
    :param card_deck: [(int, str)] list of all cards in the deck indicated by tuples
    :return: [(int, str)] shuffled card_deck
    """
    shuffled_cards = cards.copy()
    random.shuffle(shuffled_cards)
    return shuffled_cards


def compare_two_cards(card_one: (int, str), card_two: (int, str)) -> int:
    """
    returns a number encoding if card_one has a larger value than card_two

    :param card_one: first card, contains value and the color
    :type card_one: (int, str)
    :param card_two: second card, contains value and the color
    :type card_two: (int, str)
    :return: number - 0: if card_one is lower than card_two; 1: if card_one is equal card_two; 2: if card_one is larger
    than card_two;
    """
    if card_one[0] > card_two[0]:
        return 2
    elif card_one[0] == card_two[0]:
        return 1
    else:
        return 0


def compare_two_cards_trump(card_one: (int, str), card_two: (int, str), trump: str) -> int:
    """
    returns a number with declares if card_one is bigger than the other

    :param card_one: first card, contains value and the color
    :type card_one: (int, str)
    :param card_two: second card, contains value and the color
    :type card_two: (int, str)
    :param trumpf: str - color with has a bigger weight than the others
    :return: number - 0: if card_one is lower than card_two; 1: if card_one is equal card_two; 2: if card_one is bigger
    than card_two;
    """

    if card_one[1] == trump:
        # card one is trump
        if card_two[1] == trump:
            # card two is trump, check bigger number of both cards
            return compare_two_cards(card_one, card_two)
        else:
            # card two is no trump -> card one is bigger
            return 2
    elif card_two[1] == trump:
        # card one no trump & card two is trump -> card two is bigger
        return 0
    else:
        # no trumpf card - only value
        return compare_two_cards(card_one, card_two)


def hand_out_cards(list_cards: [(int, str)], players: int, number_of_cards: int) -> [[(int, str)]]:
    """
    deals the cards of the deck to the players

    :param list_cards: shuffled list
    :param players: number of players, with get cards
    :param number_of_cards: number of card per player
    :return: [[(int, str)]] - returns players sublist with the corresponding cards
    :rtype [[(int, str)]]
    """
    return_list = []
    for i in range(players):
        return_list.append(
            list_cards[i * number_of_cards:i * number_of_cards + number_of_cards])
    return return_list


def main():
    cards = create_card_list(8)  # generate list of cards with values 1 to 8
    print('Kartendeck: ')
    print(cards)
    cards_shuffled = shuffle_card_list(cards)
    print('Kartendeck gemischt: ')
    print(cards_shuffled)
    hands = hand_out_cards(cards, 3, 5)  # hand out 5 cards to 3 players each
    print('Die Karten der Spieler: ')
    print(hands)
    card1 = cards[2][:]  # get a first card
    print(card1)
    card2 = cards[7][:]  # get a second card
    print(card2)
    comp = compare_two_cards(card2, card1)  # value of card2 is larger
    print(comp)
    # value of card1 is smaller, but it's trump
    comp_trump = compare_two_cards_trump(card1, card2, "Herz")
    print(comp_trump)


if __name__ == '__main__':
    main()
