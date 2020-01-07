from father_class.piece import Piece

class King(Piece):
    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.in_check = False
        self.in_checkmate = False
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def __v_right_boxes(self, table):
        p1 = self.p1
        for p2 in range(self.p2 + 1, 7):
            box = table.c_table[p1][p2]
            if not box.is_available():
                return False
            if self.is_controlled(table, p1, p2):
                return False
        return True
    
    def __v_left_boxes(self, table):
        p1 = self.p1
        for p2 in range(self.p2 - 1, 0, -1):
            box = table.c_table[p1][p2]
            if not box.is_available():
                return False
            if self.is_controlled(table, p1, p2):
                return False
        return True

    
    def castling_to_right(self, table):
        if self.__v_right_boxes(table) and not table.c_table[self.p1][7].is_available():
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
            else:
                print('Una de las piezas que hacen el enroque se ha movido')
        else:
            print('El rey no puede hacer el enroque')

    def castling_to_left(self, table):
        if self.__v_left_boxes(table) and not table.c_table[self.p1][0].is_available():
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
            else:
                print('Una de las piezas que hacen el enroque se ha movido')
        else:
            print('El rey no puede hacer el enroque')

    def is_controlled(self, table, p1, p2):
        box = table.c_table[p1][p2]
        for p in box.controlled_by:
            if p[1] != self.color:
                return True
        return False

    def move(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and destiny.is_available():
                if not self.is_controlled(table, p1, p2):
                    table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    self.change_position(table, p1, p2)
                    self.moves+= 1
                else:
                    print('La casilla está controlada por una pieza enemiga')
            else:
                print('El movimiento que ha insertado es invalido')

    def capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and not destiny.is_available():
                f_piece = table.c_table[p1][p2].piece_in_self
                if self.is_enemy_piece(f_piece):
                    if not self.is_controlled(table, p1, p2):
                        table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                        f_piece.dead(table)
                        destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                        self.change_position(table, p1, p2)
                        self.moves+= 1
                    else:
                        print('La pieza está protegida')
                else:
                    print('Esta no es una pieza enemiga')
            else:
                print('Este no es un movimiento válido o no hay pieza para capturar')