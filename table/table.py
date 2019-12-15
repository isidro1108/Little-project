class Table:
    def __init__(self):
        self.c_table = []
    
    def create(self, turn_row = 1):
        if turn_row % 2 != 0 and turn_row < 9:
            self.c_table.append(['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'])
            return self.create(turn_row= turn_row + 1)
        elif turn_row % 2 == 0:
            self.c_table.append(['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'])
            return self.create(turn_row= turn_row + 1)
        return
        
    def is_available(self, p1, p2):
        return self.c_table[p1][p2] == '⬜' or self.c_table[p1][p2] == '⬛'

    def is_piece(self, p1, p2):
        return not self.is_available(p1, p2)