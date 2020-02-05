class Piece:
    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.value = None
        self.moves = 0
        self.movements = []
        self.controlled_boxes = []
        
    def move_in_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.movements

    def g_all_movements(self):
        pass

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

    def status(self):
        print('Color: ' + self.color)
        print('Position:', self.p1, self.p2)
        print('Value:', self.value)
        print('Moves:', self.moves)
        print('Movements:', self.movements)
        print('Controlled Boxes:', self.controlled_boxes)
    
    def move(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and destiny.is_available():
                table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                self.change_position(table, p1, p2)
                self.moves+= 1
                return True
            print('El movimiento que ha insertado es invalido')
            return False
        return False

    def capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and not destiny.is_available():
                f_piece = table.c_table[p1][p2].piece_in_self
                if self.is_enemy_piece(f_piece):
                    table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                    f_piece.dead(table)
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    self.change_position(table, p1, p2)
                    self.moves+= 1
                    return True
                print('Esta no es una pieza enemiga')
                return False
            print('Este no es un movimiento válido o no hay pieza para capturar')
            return False
        return False
    
    def dead(self, table):
        table.repository.append(self)
        for pos in self.controlled_boxes:
            table.c_table[pos[0]][pos[1]].controlled_by.remove((type(self), self.color))
        self.controlled_boxes = []

    def revert_move(self, table):
        last_p1, last_p2 = table.movement_log[-1][0][0], table.movement_log[-1][0][1]
        self.move(table, last_p1, last_p2)
        table.movement_log.pop()
        self.moves-= 2

    def revert_capture(self, table):
        last_p1, last_p2 = table.movement_log[-1][0][0], table.movement_log[-1][0][1]
        self.move(table, last_p1, last_p2)
        table.restore_piece()
        table.movement_log.pop()
        self.moves-= 2
