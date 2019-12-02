class Table:
    def create_table(self):
        matrix = []
        for row in range(0,8):
            if row == 0 or row % 2 == 0:
                matrix.append(['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'])
            else:
                matrix.append(['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'])
        return matrix
    
    def print_table(self, t):
        row = 8
        for r in t:
            print(row, '  ' + r[0], '   ' + r[1], '   ' + r[2], '   ' + r[3], '   ' + r[4], '   ' + r[5], '   ' + r[6], '   ' + r[7])
            row-= 1
        print('   ', 'a   ','b   ','c   ','d   ','e   ','f   ','g   ', 'h')