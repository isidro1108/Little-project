class Piece:
    color_p = {'white': 0, 'black': 1}

    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.moves = 0
        self.is_defended = None

class King(Piece):
    # symbols = ['♚','♔']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.in_check = False
        self.in_checkmate = False
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def move_piece(self, p1, p2):
        if (p1 - self.p1, p2 - self.p2) in self.movements:
            self.p1 = p1
            self.p2 = p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Queen(Piece):
    # symbols = ['♛','♕']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]

    def move_piece(self, p1, p2):
        if (p1 - self.p1, p2 - self.p2) in self.movements:
            self.p1 = p1
            self.p2 = p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Bishop(Piece):
    # symbols = ['♝','♗']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    
    def move_piece(self, p1, p2):
        if (p1 - self.p1, p2 - self.p2) in self.movements:
            self.p1 = p1
            self.p2 = p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Knight(Piece):
    # symbols = ['♞','♘']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(2, 1), (-2, -1), (2, -1), (-2, 1),
                        (1, 2), (-1, -2), (1, -2), (-1, 2)]
    
    def move_piece(self, p1, p2):
        if (p1 - self.p1, p2 - self.p2) in self.movements:
            self.p1 = p1
            self.p2 = p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Tower(Piece):
    # symbols = ['♜','♖']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def move_piece(self, p1, p2):
        if (p1 - self.p1, p2 - self.p2) in self.movements:
            self.p1 = p1
            self.p2 = p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Pawn(Piece):
    # symbols = ['♟','♙']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(-1, 0), (-2, 0)]
        if self.color == 'black':
            self.movements = [(1, 0), (2, 0)]
    
    def move_piece(self, p1, p2):
        if (p1 - self.p1, p2 - self.p2) in self.movements:
            self.p1 = p1
            self.p2 = p2
            self.movements = [(-1, 0)]
            if self.color == 'black':
                self.movements = [(1, 0)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

pawn = Pawn('white', 6, 4)

print(pawn.p1, pawn.p2)

pawn.move_piece(4, 4)

print(pawn.p1, pawn.p2)

pawn.move_piece(3, 4)

print(pawn.p1, pawn.p2)

