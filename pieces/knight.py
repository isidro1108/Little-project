from father_class.piece import Piece

class Knight(Piece):
    # symbols = ['♞','♘']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.movements = [(2, 1), (-2, -1), (2, -1), (-2, 1),
                        (1, 2), (-1, -2), (1, -2), (-1, 2)]
    
    def move(self, p1, p2):
        if self.move_in_movements(p1, p2):
            self.p1 = p1
            self.p2 = p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')