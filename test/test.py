import unittest
from unittest.mock import patch

from GameComponents import Board, Player, PlayerPosition, Snake, CrookedDice
from GamePlan import GamePlan


class TestRunGame(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player("Test Player")
        self.player_position = PlayerPosition(self.player.name, 0)
        self.game = GamePlan(self.board)
        self.snake = Snake(14, 7)

    def test_add_players(self):
        self.game.add_players(self.player)
        self.assertEqual(self.player.name, "Test Player")

    def test_player_position(self):
        self.assertEqual(self.player_position.position, 0)
        self.player_position.update_position(6)
        self.assertEqual(self.player_position.position, 6)

    def test_validate_snake(self):
        snake1 = Snake(10, 8)
        snake2 = Snake(9, 18)
        self.assertEqual(snake1.validate_snake_value(), True)
        self.assertEqual(snake2.validate_snake_value(), False)

    def test_is_snake_there(self):
        self.board.add_snake(self.snake)
        self.assertEqual(self.game.is_snake_there(14), 7)
        self.assertEqual(self.game.is_snake_there(4), None)

    def test_new_position_after_snake(self):
        self.board.add_snake(self.snake)
        self.assertEqual(self.game.find_new_position(9, 5), 7)
        self.assertEqual(self.game.find_new_position(15, 5), 20)

    def test_crooked_dice(self):
        crooked_dice = CrookedDice()
        self.assertEqual(crooked_dice.roll() % 2 == 0, True)

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
