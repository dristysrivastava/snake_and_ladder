from GameComponents import Board, Player, Snake
from GamePlan import GamePlan


class RunGame:
    @classmethod
    def run(cls, dice_choice):
        board = Board()

        snake = Snake(14, 7)
        if snake.validate_snake_value():
            board.add_snake(snake)

        player = Player("Test Player")
        game = GamePlan(board)
        game.add_players(player)
        dice_choice = "Dice" if dice_choice == 1 else "CrookedDice"
        game.start_game(10, dice_choice)


if __name__ == '__main__':
    try:
        dice = int(input("Enter your choice \n 1. For Normal Dice. \n 2. For Crooked Dice. \n"))
        if dice == 1:
            RunGame.run("Dice")
        elif dice == 2:
            RunGame.run("CrookedDice")
        else:
            print("Please enter correct value!!")
    except ValueError:
        print("Please enter correct value!!")
