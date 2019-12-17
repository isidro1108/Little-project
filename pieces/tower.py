from father_class.piece import Piece

class Tower(Piece):
    # symbols = ['♜','♖']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]