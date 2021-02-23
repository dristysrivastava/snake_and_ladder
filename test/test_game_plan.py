import unittest

from GameComponents import Board, Player, PlayerPosition, Snake
from GamePlan import GamePlan


class TestGamePlan(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Player("Test Player")
        self.player_position = PlayerPosition(self.player.name, 0)
        self.game = GamePlan(self.board)
        self.snake = Snake(14, 7)

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


if __name__ == '__main__':
    unittest.main()
