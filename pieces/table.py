class Table:
    def __init__(self):
        self.c_table = [['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
                        ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],
                        ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
                        ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],
                        ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
                        ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],
                        ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],
                        ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜']]
        
    def is_available(self, p1, p2):
        return self.c_table[p1][2] == '⬜' or self.c_table[p1][2] == '⬛'
    
    # def print_table(self, t):
    #     row = 8
    #     for r in t:
    #         print(row, '  ' + r[0], '   ' + r[1], '   ' + r[2], '   ' + r[3], '   ' + r[4], '   ' + r[5], '   ' + r[6], '   ' + r[7])
    #         row-= 1
    #     print('   ', 'a   ','b   ','c   ','d   ','e   ','f   ','g   ', 'h')

    # def box_is_available(self, p1, p2):
    #     if p1 >= 8 and p1 < 0:
    #         if p2 >= 8 and p2 < 0:
    #             return self.chess_table[p1][p2] == '⬜' or self.chess_table[p1][p2] == '⬛'
    #     return False