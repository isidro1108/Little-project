# This is the class box that is responsible for containing the piece
class Box:
    # Box's features
    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.piece_in_self = None
        self.controlled_by = []
    
    # Indicate if there is no piece in the box
    def is_available(self):
        return self.piece_in_self == None

    # Tells a piece if the square is controlled by another opposing piece
    def is_controlled(self, piece):
        for p in self.controlled_by:
            if p[1] != piece.color:
                return True
        return False
