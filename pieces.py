from table import Table

class Piece:
    color_p = {'white': 0, 'black': 1}

    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.moves = 0
        self.is_defended = None

class King(Piece):
    symbols = ['♚','♔']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]
        self.in_check = False
        self.in_checkmate = False
        self.movements = [(p1 + 1, p2 + 1), (p1 - 1, p2 - 1), (p1 + 1, p2 - 1), (p1 - 1, p2 + 1), 
                        (p1 + 1, p2), (p1 - 1, p2), (p1, p2 + 1), (p1, p2 - 1)]
    
    def move_piece(self, table, p1, p2):
        new_table = Table()
        empty_table = new_table.create_table()
        p_movements = []
        for movement in self.movements:
            if movement[0] < 8 and movement[0] >= 0:
                if movement[1] < 8 and movement[1] >= 0:
                    p_movements.append(movement)
        if (p1, p2) in p_movements:
            table[self.p1][self.p2] = empty_table[self.p1][self.p2]
            table[p1][p2] = self.symbol
            self.p1 = p1
            self.p2 = p2
            self.movements = [(p1 + 1, p2 + 1), (p1 - 1, p2 - 1), (p1 + 1, p2 - 1), (p1 - 1, p2 + 1), 
                                (p1 + 1, p2), (p1 - 1, p2), (p1, p2 + 1), (p1, p2 - 1)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido') 

class Queen(Piece):
    symbols = ['♛','♕']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(p1 + 1, p2 + 2), (p1 + 1, p2 - 1), (p1 - 1, p2 + 1), (p1, p2 + 1),
                        (p1 + 1, p2), (p1 - 1, p2 - 2),(p1 - 1, p2),(p1 , p2 -1)]

    def move_piece(self, table, p1, p2):
        new_table = Table()
        empty_table = new_table.create_table()
        p_movements = []
        for movement in self.movements:
            if movement[0] < 8 and movement[0] >= 0:
                if movement[1] < 8 and movement[1] >= 0:
                    p_movements.append(movement)
        if (p1, p2) in p_movements:
            table[self.p1][self.p2] = empty_table[self.p1][self.p2]
            table[p1][p2] = self.symbol
            self.p1 = p1
            self.p2 = p2
            self.movements = [(p1 + 1, p2 + 1), (p1 - 1, p2 - 1), (p1 + 1, p2 - 1), (p1 - 1, p2 + 1), 
                                (p1 + 1, p2), (p1 - 1, p2), (p1, p2 + 1), (p1, p2 - 1)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Bishop(Piece):
    symbols = ['♝','♗']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(p1 - 1, p2 - 1), (p1 + 1, p2 + 1), (p1 - 1, p2 + 1), (p1 + 1, p2 - 1)]
    
    def move_piece(self, table, p1, p2):
        new_table = Table()
        empty_table = new_table.create_table()
        p_movements = []
        for movement in self.movements:
            if movement[0] < 8 and movement[0] >= 0:
                if movement[1] < 8 and movement[1] >= 0:
                    p_movements.append(movement)
        if (p1, p2) in p_movements:
            table[self.p1][self.p2] = empty_table[self.p1][self.p2]
            table[p1][p2] = self.symbol
            self.p1 = p1
            self.p2 = p2
            self.movements = [(p1 - 1, p2 - 1), (p1 + 1, p2 + 1), (p1 - 1, p2 + 1), (p1 + 1, p2 - 1)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Knight(Piece):
    symbols = ['♞','♘']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(p1 + 2, p2 + 1), (p1 - 2, p2 - 1), (p1 + 2, p2 - 1), (p1 - 2, p2 + 1),
                        (p1 + 1, p2 + 2), (p1 - 1, p2 - 2), (p1 + 1, p2 - 2), (p1 - 1, p2 + 2)]
    
    def move_piece(self, table, p1, p2):
        new_table = Table()
        empty_table = new_table.create_table()
        p_movements = []
        for movement in self.movements:
            if movement[0] < 8 and movement[0] >= 0:
                if movement[1] < 8 and movement[1] >= 0:
                    p_movements.append(movement)
        if (p1, p2) in p_movements:
            table[self.p1][self.p2] = empty_table[self.p1][self.p2]
            table[p1][p2] = self.symbol
            self.p1 = p1
            self.p2 = p2
            self.movements = [(p1 + 2, p2 + 1), (p1 - 2, p2 - 1), (p1 + 2, p2 - 1), (p1 - 2, p2 + 1),
                            (p1 + 1, p2 + 2), (p1 - 1, p2 - 2), (p1 + 1, p2 - 2), (p1 - 1, p2 + 2)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Tower(Piece):
    symbols = ['♜','♖']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(p1 + 1, p2), (p1, p2 + 1), (p1 - 1, p2), (p1, p2 - 1)]
    
    def move_piece(self, table, p1, p2):
        new_table = Table()
        empty_table = new_table.create_table()
        p_movements = []
        for movement in self.movements:
            if movement[0] < 8 and movement[0] >= 0:
                if movement[1] < 8 and movement[1] >= 0:
                    p_movements.append(movement)
        if (p1, p2) in p_movements:
            table[self.p1][self.p2] = empty_table[self.p1][self.p2]
            table[p1][p2] = self.symbol
            self.p1 = p1
            self.p2 = p2
            self.movements = [(p1 + 1, p2), (p1, p2 + 1), (p1 - 1, p2), (p1, p2 - 1)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')

class Pawn(Piece):
    symbols = ['♟','♙']

    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.symbol = self.symbols[self.color_p[color]]
        self.movements = [(p1 - 1, p2)]
    
    def move_piece(self, table, p1, p2):
        new_table = Table()
        empty_table = new_table.create_table()
        p_movements = []
        if self.color == 'black':
            self.movements = [(self.p1 + 1, self.p2)]
        for movement in self.movements:
            if movement[0] < 8 and movement[0] >= 0:
                if movement[1] < 8 and movement[1] >= 0:
                    p_movements.append(movement)
        if self.moves == 0 and self.color == 'white':
            p_movements.append((self.p1 - 2, self.p2))
        if self.moves == 0 and self.color == 'black':
            p_movements.append((self.p1 + 2, self.p2))
        if (p1, p2) in p_movements:
            table[self.p1][self.p2] = empty_table[self.p1][self.p2]
            table[p1][p2] = self.symbol
            self.p1 = p1
            self.p2 = p2
            self.movements = [(p1 - 1, p2)]
            self.moves+= 1
        else:
            print('El movimiento que ha insertado es invalido')


table = Table()
chess_table = table.create_table()

knight = Knight('black', 0, 1)

chess_table[knight.p1][knight.p2] = knight.symbol

table.print_table(chess_table)

while True:
    knight.move_piece(chess_table, int(input('Coordenada 1: ')), int(input('Coordenada 2: ')))
    table.print_table(chess_table)