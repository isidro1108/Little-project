from piece import Piece

class Pawn(Piece):
    # symbols = ['♟','♙']
    address = {'white': -1, 'black': 1} # Direccion del peon dependiendo del color

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.dir = self.address[self.color] # Atributo que representa la direccion del peon
        self.movements = [(1 * self.dir, 0), (2 * self.dir, 0)] # Primera aplicacion del atributo dir
    
    def move(self, p1, p2):
        if self.move_in_movements(p1, p2):
            self.p1 = p1
            self.p2 = p2
            self.movements = [(1 * self.dir, 0)] # Segunda aplicacion del atributo dir
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')