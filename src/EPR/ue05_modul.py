'''
Contains functions for ue05.py
'''

__author__ = '8175858, Braun'

import ue04


def load_players():
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


def initialize_variables(players):
    '''
    Initializes the points and hand of cards for every player.
    '''
    points = {player_name: 0 for player_name in players}
    card_list = ue04.shuffle_card_list(ue04.create_card_list2(32))
    players_map = ue04.hand_out_cards(card_list, players, 4)
    return points, players_map


def play_game(players, scores, all_hands):
    '''
    Plays the game.
    '''
    def check_card(card, player_hand, trump):
        '''
        Checks if the card is playable.
        '''
        if card[1] == trump:
            return True
        for player_card in player_hand:
            if player_card[1] == trump:
                return True
        return False

    def play_card(player_hand, trump):
        '''
        plays a card if possible and returns played card and new player hand
        '''
        print(player_hand, 'player_hand')
        for card in player_hand:
            print(card)
            while True:
                to_play = input('Do you want to play this card? (y/n)')
                if to_play == 'y':
                    if check_card(card, player_hand, trump):
                        print('Card playable!')
                        player_hand.remove(card)
                        return card, player_hand
                    else:
                        print('Card not playable!')
                elif to_play == 'n':
                    break
                else:
                    print('Invalid input! Please enter either "y" or "n".')
        return None, player_hand

    print(play_card(all_hands['marv'], 'Kreuz')[1])


players = load_players()
play_game(players, 0, initialize_variables(players)[1])
