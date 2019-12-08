from pieces import Piece

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