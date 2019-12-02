# colors = {'white': 0, 'black': 1}
# pieces = {'pawn': ['♟','♙', 1], 'tower': ['♜','♖', 5], 'horse': ['♞','♘', 3], 
#           'bishop': ['♝','♗', 3], 'queen': ['♛','♕', 9], 'king': ['♚','♔', 'abstract value']}

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
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