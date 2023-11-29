'''
Contains functions for ue05.py
'''

__author__ = '8175858, Braun'

import random
import ue04


def load_players() -> [str]:    # type: ignore
    ''''
    Reads player names from the console and returns them in a list.
    '''
    players = []
    i = 1
    while (i < 5):
        players.append(input(f'Player {i}: '))
        if i == 3:
            while True:
                continue_input = input(
                    'Do you want to add another player? (y/n) ')
                if continue_input == 'y':
                    break
                elif continue_input == 'n':
                    return players
                else:
                    print('Invalid input! Try again.')
        i += 1

    return players


def initialize_variables(players: [str]) -> ({str: int}, {str: list}):  # type: ignore # noqa
    '''
    Initializes the points and hand of cards for every player.
    '''
    points = {player_name: 0 for player_name in players}
    card_list = ue04.shuffle_card_list(ue04.create_card_list2(4))
    players_map = ue04.hand_out_cards(
        card_list, players, len(card_list) // len(players))
    return points, players_map


def play_game(players: list, scores: {str: int}, all_hands: {str: list}) -> {str: int}:  # type: ignore  # noqa
    '''
    Plays the game and defines functions for playing a card, 
    determining the winner of a trick and updating the score.
    '''
    def check_card(card: (int, str), player_hand: list, trump: str) -> bool:  # type: ignore
        '''
        Checks if the card is playable.
        '''
        print('Trump:', trump)
        print('player_hand:', player_hand)
        if card[1] == trump:
            return True
        if any(player_card[1] == trump for player_card in player_hand):
            print('Trump in hand!')
            return False
        return True

    def play_card(
        player_hand: list,
        trump: str
    ) -> ((int, str), list):  # type: ignore
        '''
        plays a card if possible and returns played card and new player hand
        '''
        print('Your Hand', player_hand)
        for card in player_hand:
            while True:
                to_play = input(f'Do you want to play {card}? (y/n)')
                if to_play == 'y':
                    if trump == '':
                        player_hand.remove(card)
                        return card, player_hand
                    if check_card(card, player_hand, trump):

                        print(f'{card} played!')
                        player_hand.remove(card)
                        return card, player_hand
                    print(f'{card} not playable!')
                elif to_play == 'n':
                    break
                else:
                    print('Invalid input! Please enter either "y" or "n".')
        return None, player_hand

    # print(play_card(all_hands['marv'], 'Kreuz')[1])
    # print(all_hands['marv'], 'all_hands')

    def get_winner(current_trick: list, trump: str) -> int:
        '''
        Determines the winner of the current trick and returns the index of the winner.
        '''
        print('Current trick:', current_trick)
        print('Trump:', trump)
        winner = current_trick[0]
        for card in enumerate(current_trick, start=1):
            if card[1] == trump:
                winner = card if card[0] > winner[0] else winner
        winner_name = ''
        for name, player_cards in all_hands.items():
            for card in player_cards:
                if winner == card:
                    winner_name = name
                    return players.index(winner_name)
        return players.index(winner_name)

    def update_score(won_cards: list, player: str, scores: {str: int}) -> {str: int}:  # type: ignore # noqa
        '''
        Updates the score of the player. Gives one penalty point for every card with the suit "Kreuz". 
        Returns the new score for the winner of this trick .
        '''
        penalty_points = 0
        for card in won_cards:
            if card[1] == 'Kreuz':
                penalty_points += 1
        scores[player] += penalty_points
        return scores[player]

    # actual game
    while any(all_hands[player] for player in players):
        # defining random playing order
        playing_order = players.copy()
        random.shuffle(playing_order)

        # playing a trick
        i = 1
        print('Playing order: ', playing_order)
        print('Current player: ', playing_order[0])
        play = play_card(all_hands[playing_order[0]], '')
        trump, all_hands[playing_order[0]] = play[0][1], play[1]
        current_trick = [play[0]]
        print('Trump:', trump)
        while True:

            print('Current Player: ' + playing_order[i])
            print('Current trick: ', current_trick)
            if all_hands[playing_order[i]] == []:
                break

            play = play_card(all_hands[playing_order[i]], trump)
            while (play[0] is None):
                play = play_card(all_hands[playing_order[i]], trump)
            if play[0][1] != trump:
                break
            all_hands[playing_order[i]] = play[1]
            current_trick.append(play[0])

            i = i + 1 if i < 2 else 0
            if play[0][1] != trump:
                break

        winner = get_winner(current_trick, trump)
        print('Winner:', playing_order[winner])
        scores[winner] = update_score(
            current_trick, playing_order[winner], scores)
        trump = play[1]
    return scores


players = load_players()
play_game(players, initialize_variables(players)
          [0], initialize_variables(players)[1])
