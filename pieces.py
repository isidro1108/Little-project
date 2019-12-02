class Piece:
    colors = {'white': 0, 'black': 1}
    pieces = {'pawn': ['♟','♙', 1], 'tower': ['♜','♖', 5], 'horse': ['♞','♘', 3], 
             'bishop': ['♝','♗', 3], 'queen': ['♛','♕', 9], 'king': ['♚','♔', 'abstract value']}

    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
        self.value = self.pieces[self.name][2]
        self.symbol = self.pieces[self.name][self.colors[self.color]]
        self.moves = 0

class King(Piece):
    pass

class Queen(Piece):
    pass

class Bishop(Piece):
    pass

class Horse(Piece):
    pass

class Tower(Piece):
    pass

class Pawn(Piece):
    pass