from father_class.piece import Piece

class Knight(Piece):
    # symbols = ['♞','♘']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.movements = [(2, 1), (-2, -1), (2, -1), (-2, 1),
                        (1, 2), (-1, -2), (1, -2), (-1, 2)]