from father_class.piece import Piece

class King(Piece):
    # symbols = ['♚','♔']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.in_check = False
        self.in_checkmate = False
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def __v_right_boxes(self, table, tp2):
        p1 = self.p1
        for p2 in range(self.p2 + 1, tp2):
            if not table.c_table[p1][p2].is_available():
                return False
        return True
    
    def __v_left_boxes(self, table, tp2):
        p1 = self.p1
        for p2 in range(self.p2 - 1, tp2, -1):
            if not table.c_table[p1][p2].is_available():
                return False
        return True

    
    def castling_to_right(self, table, tp2):
        if self.__v_right_boxes(table, tp2):
            p1, p2 = self.p1, self.p2 + 2
            destiny = table.c_table[p1][p2]
            tower = table.c_table[p1][tp2].piece_in_self
            destiny_t = table.c_table[p1][p2 - 1]
            destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
            destiny_t.piece_in_self, table.c_table[p1][tp2].piece_in_self = tower, None
            self.change_position(table, p1, p2)
            tower.change_position(table, p1, p2 - 1)
            self.moves+= 1
            tower.moves+= 1
        else:
            print('El rey no puede hacer el enroque')