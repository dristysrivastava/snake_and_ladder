from GameComponents import Dice, PlayerPosition, CrookedDice


class GamePlan:
    def __init__(self, board):
        self.board = board
        self.player_position = None

    def add_players(self, player, position=0):
        self.player_position = PlayerPosition(player, position)

    def is_snake_there(self, pos):
        end_pos = None
        for snake in self.board.snake_list:
            if snake.start == pos:
                print(f"snake is here at {pos} so updated position will be {snake.end}")
                end_pos = snake.end
                break
        if not end_pos:
            for num, green_snake in enumerate(self.board.green_snake_list, start=0):
                if green_snake.start == pos:
                    if not self.board.green_snake_list[num].already_bit:
                        self.board.green_snake_list[num].already_bit = True
                        print(f"Green snake is here at {pos} so updated position will be {green_snake.end}")
                        end_pos = green_snake.end
                        break
        return end_pos

    def find_new_position(self, curr_pos, dice_value):
        new_pos = curr_pos + dice_value
        pos = self.is_snake_there(new_pos)
        if pos:
            return pos
        else:
            return new_pos

    def start_game(self, game_rounds, dice_choice):
        game_count = 0
        final_position = 0
        while game_count < game_rounds:
            dice_value = Dice.roll() if dice_choice == "Dice" else CrookedDice.roll()
            print(f"Dice roll value: {dice_value}")
            curr_pos = self.player_position
            new_pos = self.find_new_position(curr_pos.position, dice_value)
            print(new_pos)
            curr_pos.update_position(new_pos)
            print(self.player_position.player.name, 'moved from', curr_pos, 'to', new_pos)
            final_position = new_pos
            game_count += 1
        return final_position
