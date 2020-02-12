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
        # The direction of movement is obtained from 
        # the current position and the target position
        d = (int(d1/abs(d1)), int(d2/abs(d2)))
        while p1 != pd1 and p2 != pd2:
            # The unit vector obtained in the previous 
            # formula is used to check box by box until it 
            # reaches the destination position or until a 
            # occupied box is found
            check_box = (p1 + d[0], p2 + d[1]) # Check box
            box = table.c_table[check_box[0]][check_box[1]]
            if box.is_available():
                result.append(check_box)
            else:
                result.append(check_box)
                return result
            # The position values ​​are updated to the next box
            p1, p2 = p1 + d[0], p2 + d[1]
        return result # Verified boxes
