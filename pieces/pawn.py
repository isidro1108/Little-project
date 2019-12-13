from father_class.piece import Piece

class Pawn(Piece):
    # symbols = ['♟','♙']
    address = {'white': -1, 'black': 1} # Direccion del peon dependiendo del color

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.dir = self.address[self.color] # Atributo que representa la direccion del peon
        self.movements = [(1 * self.dir, 0), (2 * self.dir, 0)] # Primera aplicacion del atributo dir
    
    def move(self, table, p1, p2):
        if self.move_in_movements(p1, p2) and table.is_available(p1, p2):
            table.c_table[p1][p2], table.c_table[self.p1][self.p2] = self, self.my_box
            self.p1, self.p2 = p1, p2
            self.movements = [(1 * self.dir, 0)] # Segunda aplicacion del atributo dir
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')