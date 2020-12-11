import json
from battleship_game_classes import *


if __name__ == '__main__':
    testgame = Game(True)
    testgame.play()


# with open('data.json') as json_file:
#     data = json.load(json_file)
#
# board = Board(data['board']['rows'], data['board']['collumns'])
# player_1 = Player(data['board']['rows'],
#                   data['board']['collumns'],
#                   data['player_1']['ship_coordinates']['coordinate_1'],
#                   data['player_1']['ship_coordinates']['coordinate_2'],
#                   data['player_1']['ship_coordinates']['coordinate_3'])


# print(data['board']['rows'])

# rows = 8
# columns = 8
# board = Board(rows, columns)
# board.print_board()
# board.valid_ship_placement('d5', 'e4', 'c3')
# # print(board.is_consecutive(['d3', 'd4', 'd5']))
