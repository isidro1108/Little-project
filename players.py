from table import Table
from pieces import King
from pieces import Queen
from pieces import Bishop
from pieces import Knight
from pieces import Tower
from pieces import Pawn

class Player:
    def __init__(self, name, c_pieces):
        self.name = name
        self.c_pieces = c_pieces