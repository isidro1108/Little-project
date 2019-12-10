from pieces import Piece

class Pawn(Piece):
    # symbols = ['♟','♙']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(-1, 0), (-2, 0)]
        if self.color == 'black':
            self.movements = [(1, 0), (2, 0)]

    def __move_in_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.movements
    
    def move(self, p1, p2):
        if self.__move_in_movements(p1, p2):
            self.p1 = p1
            self.p2 = p2
            self.movements = [(-1, 0)]
            if self.color == 'black':
                self.movements = [(1, 0)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')