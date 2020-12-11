import unittest

from battleship_game_classes import *


class TestBattleshipGame(unittest.TestCase):
    def test_GameClassInstance(self):
        test_gameclass = Game(False)
        self.assertIsInstance(test_gameclass, Game)

    def test_PlayerClassInstance(self):
        test_playerclass = Player()
        self.assertIsInstance(test_playerclass, Player)

    def test_BoardClassInstance(self):
        test_boardclass = Board(None, None)
        self.assertIsInstance(test_boardclass, Board)

    def test_ShipClassInstance(self):
        test_shipclass = Ship()
        self.assertIsInstance(test_shipclass, Ship)

    def test_newGameNoPlayers(self):
        test_newgame = Game(False)
        self.assertEqual(len(test_newgame.players), 0)

    def test_newGameWithPlayers(self):
        test_newgame = Game(True)
        self.assertEqual(len(test_newgame.players), 2)

    def test_GameSequence(self):
        test_newgame = Game(True)
        test_newgame.play()
        self.assertEqual(len(test_newgame.players), 2)

    def test_newShipNoCoord(self):
        test_newship = Ship(None, None, None)
        self.assertEqual(len(test_newship.coordinates), 0)

    def test_newShipWithCoord(self):
        test_newship = Ship("B5", "B6", "B7")
        self.assertEqual(len(test_newship.coordinates), 3)

    def test_invalidShipVertical(self):
        test_newship = Ship("D5", "D9", "D6")
        self.assertFalse(test_newship.valid_ship())

    def test_invalidShipHorizontal(self):
        test_newship = Ship("F8", "A8", "B8")
        self.assertFalse(test_newship.valid_ship())

    def test_invalidShip(self):
        test_newship = Ship("F8", "A2", "B8")
        self.assertFalse(test_newship.valid_ship())

    def test_validShipVertical(self):
        test_newship = Ship("B5", "B6", "B7")
        self.assertTrue(test_newship.valid_ship())

    def test_validShipHorizontal(self):
        test_newship = Ship("B5", "C5", "D5")
        self.assertTrue(test_newship.valid_ship())

    def test_newBoardEmpty(self):
        test_newboard = Board(None, None)
        self.assertEqual(len(test_newboard.boardmatrix), 0)

    def test_newBoardNotEmpty(self):
        test_newboard = Board(4, 4)
        self.assertEqual(len(test_newboard.boardmatrix), 16)

    def test_coordInvalidFormatWrongOrder(self):
        test_newboard = Board(4, 4)
        self.assertFalse(test_newboard.valid_coordformat("7C"))

    def test_coordInvalidFormatMissingChar(self):
        test_newboard = Board(4, 4)
        self.assertFalse(test_newboard.valid_coordformat("H"))

    def test_coordValidFormat(self):
        test_newboard = Board(4, 4)
        self.assertTrue(test_newboard.valid_coordformat("D3"))

    def test_coordInvalidBoardCoordinateOutOfBounds(self):
        test_newboard = Board(4, 4)
        self.assertFalse(test_newboard.valid_boardcoord("H3"))

    def test_newPlayerNoBoard(self):
        test_newplayer = Player()
        self.assertIsNone(test_newplayer.board)

    def test_newPlayerWithBoard(self):
        test_newplayer = Player("Player1", 1, 1)
        self.assertIsNotNone(test_newplayer.board)

    def test_newPlayerNoShip(self):
        test_newplayer = Player("Player1", 1, 1)
        self.assertEqual(len(test_newplayer.ships), 0)

    def test_newPlayerWithShips(self):
        test_newplayer = Player("Player1", 3, 3, "A1", "A2", "A3")
        self.assertEqual(len(test_newplayer.ships), 1)

    def test_playerturn(self):
        test_newplayer = Player("Player1", 5, 8, "A1", "A2", "A3")
        test_newplayer.updatemyboard("B2", "Miss")
        self.assertEqual(test_newplayer.board.boardmatrix['B', 2], "Miss")

    def test_opponentturnMissed(self):
        test_newplayer = Player("Player1", 5, 8, "A1", "A2", "A3")
        self.assertEqual(test_newplayer.hitormiss("B2"), "Miss")

    def test_opponentturnHit(self):
        test_newplayer = Player("Player1", 5, 8, "A1", "A2", "A3")
        self.assertEqual(test_newplayer.hitormiss("A3"), "Hit")

    def test_opponentturnSunken(self):
        test_newplayer = Player("Player1", 5, 8, "A1", "A2", "A3")
        test_newplayer.hitormiss("A3")
        test_newplayer.hitormiss("A1")
        test_newplayer.hitormiss("A2")
        self.assertTrue(test_newplayer.ships[0].sunken())


if __name__ == '__main__':
    unittest.main()