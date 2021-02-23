import random


class Player:
    def __init__(self, name):
        self.name = name


class Board:
    def __init__(self, size=100):
        self.size = size
        self.snake_list = []
        self.green_snake_list = []

    def add_snake(self, snake):
        self.snake_list.append(snake)

    def add_green_snake(self, green_snake):
        self.green_snake_list.append(green_snake)


class Dice:
    @staticmethod
    def roll():
        return random.randint(1, 6)


class CrookedDice(Dice):
    @staticmethod
    def roll():
        return random.randrange(2, 7, 2)


class PlayerPosition:
    def __init__(self, player, position):
        self.player = player
        self.position = position

    def update_position(self, new_position):
        self.position = new_position


class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def validate_snake_value(self):
        return self.start > self.end


class GreenSnake(Snake):
    def __init__(self, start, end):
        Snake.__init__(self, start, end)
        self.already_bit = False
