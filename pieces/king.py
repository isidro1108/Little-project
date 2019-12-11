from piece import Piece

class King(Piece):
    # symbols = ['♚','♔']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        # self.symbol = self.symbols[self.color_p[color]]
        self.in_check = False
        self.in_checkmate = False
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def move(self, p1, p2):
        if self.move_in_movements(p1, p2):
            self.p1 = p1
            self.p2 = p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')
            
king = King('white', 6, 4)

print(king.p1, king.p2)

king.move(5, 4)

print(king.p1, king.p2)
