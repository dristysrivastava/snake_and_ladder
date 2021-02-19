import random


class Player:
    def __init__(self, name):
        self.name = name


class Board:
    def __init__(self, size=100):
        self.size = size
        self.snake_list = []

    def add_snake(self, snake):
        self.snake_list.append(snake)


class Dice:
    @staticmethod
    def roll():
        return random.randint(1, 6)


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
