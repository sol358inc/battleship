import string
import json


class Game:
    def __init__(self, flag):
        self.players = []
        if flag:
            # Option 1, setup game collecting info from command line
            # board_cols = input("Board setup: Please enter how many columns would you like in the board: ")
            # board_rows = input("Board setup: Please enter how many rows would you like in the board: ")
            # player1_shipcoord = input("Player1 ship placement: Please enter position of your ship, three coordinates "
            #                           "separated by comas, ex. C2, C3, C4:")
            # player2_shipcoord = input("Player2 ship placement: Please enter position of your ship, three coordinates "
            #                           "separated by comas, ex. C2, C3, C4: ")
            #
            # numberofplayers = 2     # only 2 players in a game
            # p = 0
            # while p < numberofplayers:
            #     if p == 0:
            #         self.players.append(Player("Player1", board_cols, board_rows, player1_shipcoord[0],
            #                                 player1_shipcoord[1], player1_shipcoord[2])
            #     else:
            #         self.players.append(Player("Player2", board_cols, board_rows, player2_shipcoord[0],
            #                                    player2_shipcoord[1], player2_shipcoord[2])
            #         p += 1

            # Option 2, setup game taking info from json file
            with open('data.json') as json_file:
                data = json.load(json_file)

            for player in data['players']:
                self.players.append(Player(data['players'][player]['name'],
                                           data['board']['rows'],
                                           data['board']['columns'],
                                           data['players'][player]['ship_coordinates']['coordinate_1'],
                                           data['players'][player]['ship_coordinates']['coordinate_2'],
                                           data['players'][player]['ship_coordinates']['coordinate_3']))

    def play(self):

        pass


class Board:
    def __init__(self, rows, cols):
        self.boardmatrix = {}
        if rows and cols:
            # self.boardmatrix = [[None]*cols]*rows
            self.rows = rows
            self.cols = cols
            for row in range(1, rows + 1):
                for col in string.ascii_uppercase[:cols]:
                    self.boardmatrix[col, row] = None

    def valid_coordformat(self, coord):
        if len(coord) == len(str(self.rows)) + 1:
            return coord[0].isalpha() and coord[1:].isnumeric()
        else:
            return False

    def valid_boardcoord(self, coord):
        if self.valid_coordformat(coord):
            return coord[0] in string.ascii_uppercase[:self.cols] and \
                int(coord[1:]) in range(1, self.rows + 1)

    def print_board(self):
        # optional method
        head_col = ' ' * 4
        for y in string.ascii_uppercase[:self.cols]:
            head_col = '{0}{1}  '.format(head_col, y)
        print(head_col)

        for x in range(1, self.rows + 1):
            str_row = ''
            for y in string.ascii_uppercase[:self.cols]:
                str_row = '{0}{1}  '.format(str_row, self.boardmatrix[y, x])
            print('{0}|  {1}'.format(x, str_row))


class Player:
    def __init__(self, *args):
        self.board = None
        self.ships = []
        if args:
            self.name = args[0]
            self.board = Board(args[1], args[2])
            if len(args) > 3:
                self.ships.append(Ship(args[3], args[4], args[5]))
                # print(self.ships[0].coordinates)

    def updatemyboard(self, coord_played, play_result):
        if coord_played and play_result:
            self.board.boardmatrix[coord_played[0], int(coord_played[1])] = play_result

    def hitormiss(self, coord):
        for ship in self.ships:
            return ship.hit(coord)


class Ship:
    # for simplicity purposes, assuming a valid ship has 3 coordinates
    def __init__(self, *args):
        self.coordinates = {}
        if args:
            for p in args:
                if p:
                    self.coordinates[p] = "Miss"

    def valid_ship(self):
        keys_literal = []
        keys_numbers = []
        # separate literals and numbers in given ship coordinates
        for k in self.coordinates.keys():
            keys_literal.append(k[0])
            keys_numbers.append(k[1])
        literals_list = list(set(keys_literal))     # remove duplicates from keys_literal
        literals_list.sort()
        numbers_list = list(set(keys_numbers))      # remove duplicates from keys_numbers
        keys_numbers.sort()

        if len(literals_list) == 1:
            # ship position is vertical
            return (int(keys_numbers[2]) - int(keys_numbers[1]) == abs(1)) and \
                   (int(keys_numbers[1]) - int(keys_numbers[0]) == abs(1))
        elif len(literals_list) == len(keys_literal) and len(numbers_list) == 1:
            # ship position is horizontal
            keys_literal.sort()
            return (string.ascii_uppercase.find(keys_literal[2]) -
                    string.ascii_uppercase.find(keys_literal[1]) == abs(1)) and \
                (string.ascii_uppercase.find(keys_literal[1]) -
                    string.ascii_uppercase.find(keys_literal[0]) == abs(1))
        else:
            # coordinates are not right
            return False

    def hit(self, coord):
        if coord in self.coordinates.keys():
            self.coordinates[coord] = "Hit"
            return "Hit"
        else:
            return "Miss"
        # return coord in self.coordinates.keys()

    def sunken(self):
        return list(self.coordinates.values()).count('Hit') == len(self.coordinates)
