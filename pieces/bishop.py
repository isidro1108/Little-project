from father_class.piece import Piece

class Bishop(Piece):
    # symbols = ['♝','♗']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.movements = [(-1, -1), (1, 1), (-1, 1), (1, -1)]