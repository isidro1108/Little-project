from father_class.piece import Piece

class King(Piece):
    # symbols = ['♚','♔']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.in_check = False
        self.in_checkmate = False
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]