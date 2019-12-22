class Piece:
    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.moves = 0
        self.movements = []
        self.controlled_boxes = []
        
    def move_in_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.movements

    def g_all_movements(self):
        pass

    def update(self, table):
        for row in table.c_table:
            for box in row:
                piece = box.piece_in_self
                if isinstance(piece, Piece):
                    piece.quit_control(table)
                    piece.set_control(table)

    def set_control(self, table):
        for movement in self.movements:
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                table.c_table[p1][p2].controlled_by.append((type(self), self.color))
                self.controlled_boxes.append((p1, p2))
    
    def quit_control(self, table):
        for movement in self.movements:
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                table.c_table[p1][p2].controlled_by.remove((type(self), self.color))
        self.controlled_boxes = []
    
    def change_position(self, table, p1, p2):
        self.quit_control(table)
        self.p1, self.p2 = p1, p2
        self.set_control(table)

    def is_enemy_piece(self, piece):
        return isinstance(piece, Piece) and piece.color != self.color
    
    def move(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and destiny.is_available():
                destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                self.change_position(table, p1, p2)
                self.moves+= 1
            else:
                print('El movimiento que ha insertado es invalido')

    def capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and not destiny.is_available():
                f_piece = table.c_table[p1][p2].piece_in_self
                if self.is_enemy_piece(f_piece):
                    f_piece.dead(table)
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    self.change_position(table, p1, p2)
                    self.moves+= 1
                else:
                    print('Esta no es una pieza enemiga')
            else:
                print('Este no es un movimiento válido o no hay pieza para capturar')
    
    def dead(self, table):
        table.repository.append(self)
        self.movements = []
        for pos in self.controlled_boxes:
            table.c_table[pos[0]][pos[1]].controlled_by.remove((type(self), self.color))
        self.controlled_boxes = []