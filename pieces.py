from table import Table

class Piece:
    color_p = {'white': 0, 'black': 1}

    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.moves = 0
        self.is_defended = None

class King(Piece):
    symbols = ['♚','♔']

    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.symbol = self.symbols[self.color_p[color]]

class Queen(Piece):
    symbols = ['♛','♕']

    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.symbol = self.symbols[self.color_p[color]]

class Bishop(Piece):
    symbols = ['♝','♗']

    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.symbol = self.symbols[self.color_p[color]]

class knight(Piece):
    symbols = ['♞','♘']

    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.symbol = self.symbols[self.color_p[color]]

class Tower(Piece):
    symbols = ['♜','♖']

    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.symbol = self.symbols[self.color_p[color]]

class Pawn(Piece):
    symbols = ['♟','♙']

    def __init__(self, color, position):
        Piece.__init__(self, color, position)
        self.symbol = self.symbols[self.color_p[color]]