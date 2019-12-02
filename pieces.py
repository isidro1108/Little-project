from table import Table

# colors = {'white': 0, 'black': 1}
# pieces = {'pawn': ['♟','♙', 1], 'tower': ['♜','♖', 5], 'horse': ['♞','♘', 3], 
#           'bishop': ['♝','♗', 3], 'queen': ['♛','♕', 9], 'king': ['♚','♔', 'abstract value']}

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.moves = 0
        self.is_defended = None

class King(Piece):
    color_p = {'white': 0, 'black': 1}
    symbols = ['♚','♔']

    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.symbol = self.symbols[self.color_p[color]]

class Queen(Piece):
    pass

class Bishop(Piece):
    pass

class Horse(Piece):
    pass

class Tower(Piece):
    pass

class Pawn(Piece):
    pass