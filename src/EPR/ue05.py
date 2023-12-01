"""
EPR - Exercise 05 - Card Game
"""

__author__ = '8175858, Braun'

import ue05_modul as game


def main():
    '''
    Main function. Uses functions from ue05_modul.py to play the game.
    '''
    loaded_players = game.load_players()
    points, players_map = game.initialize_variables(loaded_players)
    score = game.play_game(loaded_players, points, players_map)
    print('Game over!')
    winners = game.determine_winner(score)
    print('The winner(s) is/are:')
    for winner in winners:
        print(winner)


if __name__ == '__main__':
    main()
