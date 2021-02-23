import unittest

from GameComponents import Board, Player, PlayerPosition, Snake, CrookedDice
from GamePlan import GamePlan


class TestRunComponents(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player("Test Player")
        self.player_position = PlayerPosition(self.player.name, 0)
        self.game = GamePlan(self.board)
        self.snake = Snake(14, 7)

    def test_add_players(self):
        self.game.add_players(self.player)
        self.assertEqual(self.player.name, "Test Player")

    def test_crooked_dice(self):
        crooked_dice = CrookedDice()
        self.assertEqual(crooked_dice.roll() % 2 == 0, True)


if __name__ == '__main__':
    unittest.main()
