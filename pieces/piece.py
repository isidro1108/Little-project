class Piece:
    color_p = {'white': 0, 'black': 1}

    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.moves = 0
        self.is_defended = None
        self.movements = []
        
    def move_in_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.movements
        
    