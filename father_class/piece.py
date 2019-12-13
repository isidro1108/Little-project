class Piece:
    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.moves = 0
        self.is_defended = None
        self.my_box = None
        self.movements = []
        
    def move_in_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.movements
    
    def move(self, table, p1, p2):
        if self.move_in_movements(p1, p2) and table.is_available(p1, p2):
            table.c_table[p1][p2], table.c_table[self.p1][self.p2] = self, self.my_box
            self.p1, self.p2 = p1, p2
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')