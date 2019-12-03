from table import Table

class Piece:
    color_p = {'white': 0, 'black': 1}

    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.moves = 0
        self.is_defended = None

class King(Piece):
    symbols = ['♚','♔']

    def __init__(self, color, p1, p2):
        piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]

class Queen(Piece):
    symbols = ['♛','♕']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]
        self.moves = [(p1 + 1, p2 + 2), (p1 + 1, p2 - 1), (p1 - 1, p2 + 1), (p1, p2 + 1),(p1 + 1, p2), (p1 - 1, p2 - 2),(p1 - 1, p2),(p1 , p2 -1) ]

class Bishop(Piece):
    symbols = ['♝','♗']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]

class Knight(Piece):
    symbols = ['♞','♘']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]

class Tower(Piece):
    symbols = ['♜','♖']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]

class Pawn(Piece):
    symbols = ['♟','♙']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]