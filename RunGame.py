from GameComponents import Board, Player, Snake
from GamePlan import GamePlan


class RunGame:
    @classmethod
    def run(cls):
        board = Board()

        snake = Snake(14, 7)
        if snake.validate_snake_value():
            board.add_snake(snake)

        player = Player("Test Player")
        game = GamePlan(board)
        game.add_players(player)
        game.start_game(10)


if __name__ == '__main__':
    RunGame.run()
