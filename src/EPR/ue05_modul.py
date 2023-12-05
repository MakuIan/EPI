"""
Contains functions for ue05.py
"""

__author__ = "8175858, Braun"

import random
import ue04
import spielkarten


def load_players() -> list[str]:
    """'
    Reads player names from the console and returns them in a list.
    """
    loaded_players = []
    i = 1
    while i < 5:
        loaded_players.append(input(f"Player {i}: "))
        if i == 3:
            while True:
                continue_input = input(
                    "Do you want to add another player? (y/n) ")
                if continue_input == "y":
                    break
                if continue_input == "n":
                    return loaded_players
                print("Invalid input! Try again.")
        i += 1

    return loaded_players


def initialize_variables(
    loaded_players: list[str],
) -> tuple[dict[str, int], dict[str, list]]:
    """
    Initializes the points and hand of cards for every player.
    """
    points = {player_name: 0 for player_name in loaded_players}
    card_list = ue04.shuffle_card_list(spielkarten.create_card_list(4))
    players_map = ue04.hand_out_cards(
        # rewritten to use hand_out_cards from ue04 to return a dict
        card_list,
        loaded_players,
        len(card_list) // len(loaded_players),
    )
    return points, players_map


def play_game(
    players: list, scores: dict[str, int], all_hands: dict[str, list]
) -> dict[str, int]:
    """
    Plays the game and defines functions for playing a card,
    determining the winner of a trick and updating the score.
    """

    def check_card(card: tuple[int, str], player_hand: list, trump: str) -> bool:
        """
        Checks if the card is playable.
        """
        if card[1] == trump:
            return True
        if any(player_card[1] == trump for player_card in player_hand):
            print("Trump in hand!")
            return False
        return True

    # Tests

    def play_card(player_hand: list, trump: str) -> tuple[tuple[int, str], list] | None:
        """
        plays a card if possible and returns played card and new player hand
        """
        print("Your Hand:", player_hand)
        print("Trump:", trump)
        for card in player_hand:
            while True:
                to_play = input(f"Do you want to play {card}? (y/n)")
                if to_play == "y":
                    if trump == "":
                        player_hand.remove(card)
                        return card, player_hand
                    if check_card(card, player_hand, trump):
                        print(f"{card} played!")
                        player_hand.remove(card)
                        return card, player_hand
                    print(f"{card} not playable!")
                elif to_play == "n":
                    break
                else:
                    print('Invalid input! Please enter either "y" or "n".')
        return None

    def get_winner(current_trick: list, trump: str) -> int:
        """
        Determines the winner of the current trick and returns the index of the winner.
        """
        winner = current_trick[0][0]

        for player_played_cards in current_trick:
            for card in player_played_cards:
                if card[1] == trump:
                    winner = card if card[0] > winner[0] else winner
        winner_index = 0
        for plauer_played_cards in current_trick:
            for card in plauer_played_cards:
                if card == winner:
                    winner_index = current_trick.index(plauer_played_cards)
                    break
        return winner_index

    def update_score(
        won_cards: list, player: str, scores: dict[str, int]
    ) -> dict[str, int]:
        """
        Updates the score of the player. Gives one penalty point for every card with the suit "Kreuz".Returns the new score for the winner of this trick .
        """
        penalty_points = 0
        print("won_cards:", won_cards)
        for cards in won_cards:
            for card in cards:
                if card[1] == "Kreuz":
                    penalty_points += 1
        scores[player] -= penalty_points
        # adding card to winners hand
        flattened_list = [card for cards in won_cards for card in cards]
        all_hands[player] += flattened_list
        print("all_hands:", all_hands)
        return scores

    # actual game
    while any(all_hands[player] for player in players if all_hands[player] != []):
        # defining random playing order
        playing_order = players.copy()
        random.shuffle(playing_order)

        # playing a trick
        i = 1
        print("Playing order: ", playing_order)
        print("Current player: ", playing_order[0])
        try:
            play = None
            while play is None:
                play = play_card(all_hands[playing_order[0]], "")
            if play[1] == []:
                print("Scores:", scores)
                return scores
            trump, all_hands[playing_order[0]] = play[0][1], play[1]
        except TypeError:
            return scores
        current_trick = [[play[0]]]
        print("Trump:", trump)
        while True:
            print("Current Player: " + playing_order[i])
            print("Current trick: ", current_trick)
            if all_hands[playing_order[i]] == []:
                break

            play = None
            while play is None:
                play = play_card(all_hands[playing_order[i]], trump)
            # check if player has no cards left after he played his card
            if play[1] == []:
                print("Scores:", scores)
                return scores
            if play[0][1] != trump:
                break
            all_hands[playing_order[i]] = play[1]
            # current_trick can only have as much sublists as there are players
            if len(current_trick) <= len(playing_order):
                current_trick.append([play[0]])
            else:
                current_trick[i].append(play[0])

            i = i + 1 if i < 2 else 0
            if play[0][1] != trump:
                break
        print("Trick over!")
        winner_index = get_winner(current_trick, trump)
        winner = playing_order[winner_index]
        print("Winner:", playing_order[winner_index])
        scores = update_score(current_trick, winner, scores)
        trump = play[1]
        print("Scores:", scores)
    return scores


def determine_winner(scores: dict) -> list:
    """
    Determines the winner of the game.
    """
    return [winner for winner, score in scores.items() if score == max(scores.values())]


if __name__ == "__main__":
    # Tests
    player_list1 = load_players()
    player_list2 = load_players()
    player_list3 = load_players()
    print("player list1:", player_list1)
    print("player list2:", player_list2)
    print("player list3:", player_list3)
    print("initialize_variables")
    variables1 = initialize_variables(player_list1)
    variables2 = initialize_variables(player_list2)
    variables3 = initialize_variables(player_list3)
    print("initialize_variables 1:", variables1)
    print("initialize_variables 2:", variables2)
    print("initialize_variables 3:", variables3)
    print("play_game")
    game1 = play_game(player_list1, variables1[0], variables1[1])
    print("game1:", game1)
    game2 = play_game(player_list2, variables2[0], variables2[1])
    print("game2:", game2)
    game3 = play_game(player_list3, variables3[0], variables3[1])
    print("game3:", game3)
    print("determine_winner")
    winner1 = determine_winner({"a": 0, "b": -2, "c": -3, "d": -4})
    print("winner1:", winner1)
    winner2 = determine_winner({"a": 0, "b": 0, "c": -3, "d": -4})
    print("winner2:", winner2)
    winner3 = determine_winner({"a": 0, "b": 0, "c": 0, "d": -4})
