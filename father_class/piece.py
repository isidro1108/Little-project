class Piece:
    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.moves = 0
        self.movements = []
        
    def move_in_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.movements

    def set_control(self, table):
        for movement in self.movements:
                p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
                if (p1 < 8 and p1 >= 0) and (p2 < 8 and p2 >= 0):
                    table.c_table[p1][p2].controlled_by.append((type(self), self.color))
    
    def __quit_control(self, table):
        for movement in self.movements:
                p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
                if (p1 < 8 and p1 >= 0) and (p2 < 8 and p2 >= 0):
                    table.c_table[p1][p2].controlled_by.remove((type(self), self.color))
    
    def move(self, table, p1, p2):
        destiny = table.c_table[p1][p2]
        if self.move_in_movements(p1, p2) and destiny.is_available():
            destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
            self.__quit_control(table)
            self.p1, self.p2 = p1, p2
            self.set_control(table)
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

    def capture(self, table, p1, p2):
        destiny = table.c_table[p1][p2]
        if self.move_in_movements(p1, p2) and not destiny.is_available():
            f_piece = table.c_table[p1][p2].piece_in_self
            is_enemy_piece = isinstance(f_piece, Piece) and f_piece.color != self.color
            if is_enemy_piece:
                table.repository.append(f_piece)
                f_piece, table.c_table[self.p1][self.p2].piece_in_self = self, None
                self.__quit_control(table)
                self.p1, self.p2 = p1, p2
                self.set_control(table)
                self.moves+= 1
            else:
                print('Esta no es una pieza enemiga')
        else:
            print('Este no es un movimiento válido o no hay pieza para capturar')