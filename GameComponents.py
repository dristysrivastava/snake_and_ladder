import random


class Player:
    def __init__(self, name):
        self.name = name


class Board:
    def __init__(self, size=100):
        self.size = size


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
