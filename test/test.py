import unittest

from GameComponents import Board, Player, PlayerPosition
from GamePlan import GamePlan


class TestRunGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player("Test Player")
        self.player_position = PlayerPosition(self.player.name, 0)
        self.game = GamePlan(self.board)

    def test_add_players(self):
        self.game.add_players(self.player)
        self.assertEqual(self.player.name, "Test Player")

    def test_player_position(self):
        self.assertEqual(self.player_position.position, 0)
        self.player_position.update_position(6)
        self.assertEqual(self.player_position.position, 6)


if __name__ == '__main__':
    unittest.main()