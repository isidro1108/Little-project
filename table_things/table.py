from table_things.box import Box

class Table:
    def __init__(self):
        self.c_table = []
        self.movement_log = []
        self.repository = []
    
    def create(self, turn_row = 1):
        p1 = turn_row - 1
        if turn_row % 2 != 0 and turn_row < 9:
            self.c_table.append([Box('white', p1, 0),Box('black', p1, 1),
                                Box('white', p1, 2),Box('black', p1, 3),
                                Box('white', p1, 4),Box('black', p1, 5),
                                Box('white', p1, 6),Box('black', p1, 7)])
            return self.create(turn_row= turn_row + 1)
        elif turn_row % 2 == 0:
            self.c_table.append([Box('black', p1, 0),Box('white', p1, 1),
                                Box('black', p1, 2),Box('white', p1, 3),
                                Box('black', p1, 4),Box('white', p1, 5),
                                Box('black', p1, 6),Box('white', p1, 7)])
            return self.create(turn_row= turn_row + 1)
        return
    
    def move_is_inside(self, p1, p2):
        return (p1 < 8 and p1 >= 0) and (p2 < 8 and p2 >= 0)

    def is_controlled(self, piece, p1, p2):
        box = self.c_table[p1][p2]
        for p in box.controlled_by:
            if p[1] != piece.color:
                return True
        return False

    def v_kings(self, piece):
        for row in self.c_table:
            for box in row:
                piece = box.piece_in_self
                if piece != None and piece.value == None:
                    if piece.is_controlled(self, piece.p1, piece.p2):
                        piece.in_check = True
                    else:
                        piece.in_check = False

    def update(self):
        for row in self.c_table:
            for box in row:
                piece = box.piece_in_self
                if piece != None:
                    piece.quit_control(self)
                    piece.set_control(self)
        self.v_kings(self)