from father_class.piece import Piece

# This class inherits from the parent class Piece 
# and brings together all the common characteristics of 
# the Queen, the Tower and the Bishop
class Mpiece(Piece):
    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.dir_movements = [] # Direction of the movements

    # Get the movements around one direction recursively
    def g_movements(self, m1, m2, d1, d2):
        if (abs(m1) == 7) or (abs(m2) == 7):
            return
        else:
            self.movements.append((m1 + d1, m2 + d2))
            return self.g_movements(m1 + d1, m2 + d2, d1, d2)
    
    # Using the g_movements method, get all movement patterns in all directions
    def g_all_movements(self):
        for m in range(0, len(self.dir_movements)):
            m1, m2 = self.movements[m][0], self.movements[m][1]
            d1, d2 = self.dir_movements[m][0], self.dir_movements[m][1]
            self.g_movements(m1, m2, d1, d2)

    # method to overwrite (check the boxes where the Queen, the Tower and the Bishop can move)
    def v_boxes(self, table, p1, p2, pd1, pd2):
        return []

    def set_control(self, table):
        for movement in self.movements:
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                v_boxes = self.v_boxes(table, self.p1, self.p2, p1, p2)
                if (p1, p2) in v_boxes:
                    table.c_table[p1][p2].controlled_by.append((type(self), self.color))
                    self.controlled_boxes.append((p1, p2))

    def change_position(self, table, p1, p2):
        self.quit_control(table)
        self.p1, self.p2 = p1, p2
        self.set_control(table)

    def move(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and destiny.is_available():
                v_boxes = self.v_boxes(table, self.p1, self.p2, p1, p2)
                if (p1, p2) in v_boxes:
                    table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    self.change_position(table, p1, p2)
                    self.moves+= 1
                    return True
                table.alert = 'This piece cannot jump over another piece'
                return False
            table.alert = 'Invalid movement'
            return False
        return False

    def capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and not destiny.is_available():
                f_piece = table.c_table[p1][p2].piece_in_self
                if self.is_enemy_piece(f_piece):
                    v_boxes = self.v_boxes(table, self.p1, self.p2, p1, p2)
                    if (p1, p2) in v_boxes:
                        table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                        f_piece.dead(table)
                        destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                        self.change_position(table, p1, p2)
                        self.moves+= 1
                        return True
                    table.alert = 'This piece cannot jump over another piece'
                    return False
                table.alert = 'This is not a enemy piece'
                return False
            table.alert = 'Invalid movement or there is no piece to capture'
            return False
        return False
