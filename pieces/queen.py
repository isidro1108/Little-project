from father_class.piece import Piece
from pieces.bishop import Bishop
from pieces.tower import Tower

class Queen(Piece):
    # symbols = ['♛','♕']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.dir_movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                            (1, 0), (-1, 0), (0, 1), (0, -1)]
        self.movements = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                        (1, 0), (-1, 0), (0, 1), (0, -1)]

    def g_movements(self, m1, m2, d1, d2):
        if (abs(m1) == 7) or (abs(m2) == 7):
            return
        else:
            self.movements.append((m1 + d1, m2 + d2))
            return self.g_movements(m1 + d1, m2 + d2, d1, d2)
    
    def g_all_movements(self):
        for m in range(0, len(self.dir_movements)):
            m1, m2 = self.movements[m][0], self.movements[m][1]
            d1, d2 = self.dir_movements[m][0], self.dir_movements[m][1]
            self.g_movements(m1, m2, d1, d2)

    def v_boxes(self, table, p1, p2, pd1, pd2):
        d1, d2 = pd1 - p1, pd2 - p2
        if d1 == 0 or d2 == 0:
            return Tower.v_boxes(Tower, table, p1, p2, pd1, pd2)
        else:
            return Bishop.v_boxes(Bishop, table, p1, p2, pd1, pd2)

    def set_control(self, table):
        for movement in self.movements:
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                v_boxes = self.v_boxes(table, self.p1, self.p2, p1, p2)
                if (p1, p2) in v_boxes:
                    table.c_table[p1][p2].controlled_by.append((type(self), self.color))
                    self.controlled_boxes.append((p1, p2))

    def quit_control(self, table):
        for movement in self.movements:
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                if (p1, p2) in self.controlled_boxes:
                    table.c_table[p1][p2].controlled_by.remove((type(self), self.color))
        self.controlled_boxes = []

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
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    self.change_position(table, p1, p2)
                    self.moves+= 1
                else:
                    print('La dama no puede saltar por encima de otra ficha')
            else:
                print('El movimiento que ha insertado es invalido')

    def capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and not destiny.is_available():
                f_piece = table.c_table[p1][p2].piece_in_self
                if self.is_enemy_piece(f_piece):
                    v_boxes = self.v_boxes(table, self.p1, self.p2, p1, p2)
                    if (p1, p2) in v_boxes:
                        f_piece.dead(table)
                        destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                        self.change_position(table, p1, p2)
                        self.moves+= 1
                    else:
                        print('La dama no puede saltar por encima de otra ficha')
                else:
                    print('Esta no es una pieza enemiga')
            else:
                print('Este no es un movimiento válido o no hay pieza para capturar')