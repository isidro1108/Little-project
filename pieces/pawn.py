from father_class.piece import Piece

class Pawn(Piece):
    # symbols = ['♟','♙']
    address = {'white': -1, 'black': 1} # Direccion del peon dependiendo del color

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.dir = self.address[self.color] # Atributo que representa la direccion del peon
        self.movements = [(self.dir, 0), (2 * self.dir, 0)] # Primera aplicacion del atributo dir
        self.c_movements = [(self.dir, -1), (self.dir, 1)]
    
    def __move_in_c_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.c_movements
    
    def move(self, table, p1, p2):
        destiny = table.c_table[p1][p2]
        if self.move_in_movements(p1, p2) and destiny.is_available():
            if (p1 - self.p1, p2 - self.p2) == (2 * self.dir, 0) and not table.c_table[p1 - self.dir][p2].is_available():
                print('El peon no puede pasar por encima de sus fichas')
                return
            destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
            self.p1, self.p2 = p1, p2
            self.movements = [(self.dir, 0)] # Segunda aplicacion del atributo dir
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