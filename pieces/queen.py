from father_class.mpiece import Mpiece
from pieces.bishop import Bishop
from pieces.tower import Tower

class Queen(Mpiece):
    # symbols = ['♛','♕']

    def __init__(self, color, p1, p2):
        Mpiece.__init__(self, color, p1, p2)
        self.dir_movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                            (1, 0), (-1, 0), (0, 1), (0, -1)]
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]

    def v_boxes(self, table, p1, p2, pd1, pd2):
        d1, d2 = pd1 - p1, pd2 - p2
        if d1 == 0 or d2 == 0:
            return Tower.v_boxes(Tower, table, p1, p2, pd1, pd2)
        else:
            return Bishop.v_boxes(Bishop, table, p1, p2, pd1, pd2)