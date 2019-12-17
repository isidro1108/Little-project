class Box:
    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.piece_in_self = None
        self.controlled_by = []
    
    def is_available(self):
        return self.piece_in_self == None