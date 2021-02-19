from GameComponents import Dice, PlayerPosition


class GamePlan:
    def __init__(self, board):
        self.board = board
        self.player_position = None

    def add_players(self, player, position=0):
        self.player_position = PlayerPosition(player, position)

    def start_game(self):
        game_round = 0
        while game_round < 10:
            dice_count = Dice.roll()
            print(f"Dice roll value: {dice_count}")
            curr_pos = self.player_position
            new_pos = curr_pos.position + dice_count
            print(new_pos)
            curr_pos.update_position(new_pos)
            print(self.player_position.player.name, 'moved from', curr_pos, 'to', new_pos)
            game_round += 1
