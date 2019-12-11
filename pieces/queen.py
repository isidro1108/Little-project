from piece import Piece

class Queen(Piece):
    # symbols = ['♛','♕']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]

    def __move_in_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.movements
    
    def move(self, p1, p2):
        if self.__move_in_movements(p1, p2):
            self.p1 = p1
            self.p2 = p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')