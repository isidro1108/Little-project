from table import Table
import pieces
from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.tower import Tower
from pieces.pawn import Pawn

class Player:
    def __init__(self, name):
        self.name = name

class Player1(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.pieces = {'king': King('white', 7, 4), 'queen': Queen('white', 7, 3),
                        'bishops': [Bishop('white', 7, 2), Bishop('white', 7, 5)], 
                        'knights': [Knight('white', 7, 1), Knight('white', 7, 6)],
                        'towers': [Tower('white', 7, 0), Tower('white', 7, 7)], 
                        'pawns': [Pawn('white', 6, 0), Pawn('white', 6, 1), 
                                Pawn('white', 6, 2), Pawn('white', 6, 3),
                                Pawn('white', 6, 4), Pawn('white', 6, 5),
                                Pawn('white', 6, 6), Pawn('white', 6, 7)]}

class Player2(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.pieces = {'king': King('black', 1, 4), 'queen': Queen('black', 1, 3),
                        'bishops': [Bishop('black', 1, 2), Bishop('black', 1, 5)], 
                        'knights': [Knight('black', 1, 1), Knight('black', 1, 6)],
                        'towers': [Tower('black', 1, 0), Tower('black', 1, 7)], 
                        'pawns': [Pawn('black', 2, 0), Pawn('black', 2, 1), 
                                Pawn('black', 2, 2), Pawn('black', 2, 3),
                                Pawn('black', 2, 4), Pawn('black', 2, 5),
                                Pawn('black', 2, 6), Pawn('black', 2, 7)]