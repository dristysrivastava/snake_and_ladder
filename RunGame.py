from GameComponents import Board, Player
from GamePlan import GamePlan


class RunGame:
    @classmethod
    def run(cls):
        board = Board()
        player = Player("Test Player")
        game = GamePlan(board)
        game.add_players(player)
        game.start_game()


if __name__ == '__main__':
    RunGame.run()
