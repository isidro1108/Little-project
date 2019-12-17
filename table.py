from box import Box

class Table:
    def __init__(self):
        self.c_table = []
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