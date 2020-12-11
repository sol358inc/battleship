from battleship_game_classes import *


if __name__ == '__main__':
    newgame = Game(True)
    endofgame = False
    i = 0
    while not endofgame:
        playerinturn = newgame.players[i]
        oponent = newgame.players[i+1]

        playershot = input(playerinturn.name + ", it is your turn to play, please enter your move, ex:C5. "
                                               "Remember the board has " + str(playerinturn.board.cols) +
                           " columns and " + str(playerinturn.board.rows) + " rows: ")
        playerinturn.updatemyboard(playershot.capitalize(), oponent.hitormiss(playershot.capitalize()))

        for sh in oponent.ships:
            if sh.sunken():
                print("You have sunken my ship")
                print("Game over :-(")
                endofgame = True
                exit()

        if i == 0:
            i -= 1
        else:
            i += 1

        print(oponent.hitormiss(playershot.capitalize()))
        playerinturn.board.print_board()
