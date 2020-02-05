from father_class.mpiece import Mpiece

class Bishop(Mpiece):
    def __init__(self, color, p1, p2):
        Mpiece.__init__(self, color, p1, p2)
        self.value = 3
        self.dir_movements = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        self.movements = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    def v_boxes(self, table, p1, p2, pd1, pd2):
        result = []
        d1, d2 = pd1 - p1, pd2 - p2
        d = (int(d1/abs(d1)), int(d2/abs(d2)))
        while p1 != pd1 and p2 != pd2:
            v_box = (p1 + d[0], p2 + d[1])
            box = table.c_table[v_box[0]][v_box[1]]
            if box.is_available():
                result.append(v_box)
            else:
                result.append(v_box)
                return result
            p1, p2 = p1 + d[0], p2 + d[1]
        return result