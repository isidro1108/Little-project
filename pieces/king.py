from father_class.piece import Piece

class King(Piece):
    # Additional features
    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.in_check = False # <--
        self.in_checkmate = False # <--
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Check the boxes between the king and the right tower
    def __v_right_boxes(self, table):
        p1 = self.p1
        for p2 in range(self.p2 + 1, 7):
            box = table.c_table[p1][p2]
            if not box.is_available() or box.is_controlled(self):
                return False
        return True
    
    # Check the boxes between the king and the left tower 
    def __v_left_boxes(self, table):
        p1 = self.p1
        for p2 in range(self.p2 - 1, 0, -1):
            box = table.c_table[p1][p2]
            if not box.is_available() or box.is_controlled(self):
                return False
        return True

    # Do the right castling
    def castling_to_right(self, table):
        if self.__v_right_boxes(table) and not table.c_table[self.p1][7].is_available():
            if self.in_check == False:
                p1, p2 = self.p1, self.p2 + 2
                destiny = table.c_table[p1][p2]
                tower = table.c_table[p1][7].piece_in_self
                destiny_t = table.c_table[p1][p2 - 1]
                if tower.moves == 0 and self.moves == 0:
                    table.movement_log.append(['0 - 0'])
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    destiny_t.piece_in_self, table.c_table[p1][7].piece_in_self = tower, None
                    self.change_position(table, p1, p2)
                    tower.change_position(table, p1, p2 - 1)
                    self.moves+= 1
                    tower.moves+= 1
                    return True
                table.alert = 'One of the pieces that make the castling has moved'
                return False
            table.alert = 'The king is in check'
            return False
        table.alert = 'The king cannot do the castling'
        return False

    # Do the left castling
    def castling_to_left(self, table):
        if self.__v_left_boxes(table) and not table.c_table[self.p1][0].is_available():
            if self.in_check == False:
                p1, p2 = self.p1, self.p2 - 2
                destiny = table.c_table[p1][p2]
                tower = table.c_table[p1][0].piece_in_self
                destiny_t = table.c_table[p1][p2 + 1]
                if tower.moves == 0 and self.moves == 0:
                    table.movement_log.append(['0 - 0 - 0'])
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    destiny_t.piece_in_self, table.c_table[p1][0].piece_in_self = tower, None
                    self.change_position(table, p1, p2)
                    tower.change_position(table, p1, p2 + 1)
                    self.moves+= 1
                    tower.moves+= 1
                    return True
                table.alert = 'One of the pieces that make the castling has moved'
                return False
            table.alert = 'The king is in check'
            return False
        table.alert = 'The king cannot do the castling'
        return False

    # Change the king's position
    def change_position(self, table, p1, p2):
        self.quit_control(table)
        self.p1, self.p2 = p1, p2
        table.pos_kings[self.color] = (p1, p2)
        self.set_control(table)

    # Move the king
    def move(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and destiny.is_available():
                if not destiny.is_controlled(self):
                    table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    self.change_position(table, p1, p2)
                    self.moves+= 1
                    return True
                table.alert = 'The box is controlled by an enemy piece'
                return False
            table.alert = 'Invalid movement'
            return False
        return False

    # It Capture another piece with this piece (king)
    def capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and not destiny.is_available():
                f_piece = table.c_table[p1][p2].piece_in_self
                if self.is_enemy_piece(f_piece):
                    if not destiny.is_controlled(self):
                        table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                        f_piece.dead(table)
                        destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                        self.change_position(table, p1, p2)
                        self.moves+= 1
                        return True
                    table.alert = 'The piece is protected'
                    return False
                table.alert = 'This is not a enemy piece'
                return False
            table.alert = 'Invalid movement or there is no piece to capture'
            return False
        return False
