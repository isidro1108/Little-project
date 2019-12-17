from father_class.piece import Piece

class Pawn(Piece):
    address = {'white': -1, 'black': 1}

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.dir = self.address[self.color]
        self.movements = [(self.dir, 0), (2 * self.dir, 0)]
        self.c_movements = [(self.dir, -1), (self.dir, 1)]
        self.p_step_capture = False
    
    def __move_in_c_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.c_movements

    def __is_two_step(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) == (2 * self.dir, 0)

    def set_control(self, table):
        for movement in self.c_movements:
                p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
                if (p1 < 8 and p1 >= 0) and (p2 < 8 and p2 >= 0):
                    table.c_table[p1][p2].controlled_by.append((type(self), self.color))
    
    def __quit_control(self, table):
        for movement in self.c_movements:
                p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
                if (p1 < 8 and p1 >= 0) and (p2 < 8 and p2 >= 0):
                    table.c_table[p1][p2].controlled_by.remove((type(self), self.color))
    
    def move(self, table, p1, p2):
        destiny = table.c_table[p1][p2]
        if self.move_in_movements(p1, p2) and destiny.is_available():
            if self.__is_two_step(p1, p2) and not table.c_table[p1 - self.dir][p2].is_available():
                print('El peon no puede pasar por encima de sus fichas')
                return
            if self.__is_two_step(p1, p2):
                self.p_step_capture = True
            else:
                self.p_step_capture = False
            destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
            self.p1, self.p2 = p1, p2
            self.movements = [(self.dir, 0)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

    def capture(self, table, p1, p2):
        destiny = table.c_table[p1][p2]
        if self.__move_in_c_movements(p1, p2) and not destiny.is_available():
            f_piece = table.c_table[p1][p2].piece_in_self
            is_enemy_piece = isinstance(f_piece, Piece) and f_piece.color != self.color
            if is_enemy_piece:
                table.repository.append(f_piece)
                f_piece, table.c_table[self.p1][self.p2].piece_in_self = self, None
                self.p1, self.p2 = p1, p2
                self.moves+= 1
            else:
                print('Esta no es una pieza enemiga')
        else:
            print('Este no es un movimiento válido o no hay pieza para capturar')
        
    def step_capture(self, table, p1, p2):
        destiny = table.c_table[p1][p2]
        c_destiny = table.c_table[p1 - self.dir][p2]
        f_piece = table.c_table[p1 - self.dir][p2].piece_in_self
        if self.__move_in_c_movements(p1, p2) and destiny.is_available() and not c_destiny.is_available():
            is_enemy_piece = isinstance(f_piece, Piece) and f_piece.color != self.color
            if is_enemy_piece and f_piece.p_step_capture:
                table.repository.append(f_piece)
                c_destiny.piece_in_self, destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = None, self, None
                self.p1, self.p2 = p1, p2
                self.moves+= 1
            else:
                print('Esta no es una pieza enemiga o no se puede capturar al paso')
        else:
            print('Este no es un movimiento válido o no hay pieza para capturar')