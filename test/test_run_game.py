import unittest
from unittest.mock import patch

from GameComponents import Board, Player, PlayerPosition, Snake
from GamePlan import GamePlan


class TestRunGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player("Test Player")
        self.player_position = PlayerPosition(self.player.name, 0)
        self.game = GamePlan(self.board)
        self.snake = Snake(14, 7)

    @patch('GameComponents.Dice.roll')
    def test_run(self, mock_dice_roll):
        mock_dice_roll.return_value = 3
        self.game.add_players(self.player)
        self.assertEqual(self.game.start_game(4, "Dice"), 12)

    @patch('GameComponents.CrookedDice.roll')
    def test_run_crooked_dice(self, mock_dice_roll):
        mock_dice_roll.return_value = 6
        self.game.add_players(self.player)
        self.assertEqual(self.game.start_game(4, "CrookedDice"), 24)


if __name__ == '__main__':
    unittest.main()
