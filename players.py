from table import Table
from box import Box
from father_class.piece import Piece
from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.tower import Tower
from pieces.pawn import Pawn

class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = []
    
    def insert_pieces(self, table):
        for piece in self.pieces:
            table.c_table[piece.p1][piece.p2].piece_in_self = piece
            piece.g_all_movements()
            piece.set_control(table)

    def move(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        piece.move(table, pd1, pd2)
        piece.update(table)
    
    def capture(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        piece.capture(table, pd1, pd2)
        piece.update(table)

    def step_capture(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        if isinstance(piece, Pawn):
            piece.step_capture(table, pd1, pd2)
            piece.update(table)
        else:
            print('Esta pieza no es un peón')
    
    def castling_to_left(self, table, p1, p2):
        piece = table.c_table[p1][p2].piece_in_self
        if isinstance(piece, King):
            piece.castling_to_left(table)
            piece.update(table)
        else:
            print('Esta pieza no es un rey')
    
    def castling_to_right(self, table, p1, p2):
        piece = table.c_table[p1][p2].piece_in_self
        if isinstance(piece, King):
            piece.castling_to_right(table)
            piece.update(table)
        else:
            print('Esta pieza no es un rey')

class Player1(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.pieces = [Pawn('white', 6, 0), Pawn('white', 6, 1), 
                        Pawn('white', 6, 2), Pawn('white', 6, 3),
                        Pawn('white', 6, 4), Pawn('white', 6, 5),
                        Pawn('white', 6, 6), Pawn('white', 6, 7),
                        King('white', 7, 4), Bishop('white', 7, 2), 
                        Bishop('white', 7, 5), Knight('white', 7, 1), 
                        Knight('white', 7, 6), Tower('white', 7, 0), 
                        Tower('white', 7, 7), Queen('white', 7, 3)]

class Player2(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.pieces = [Pawn('black', 1, 0), Pawn('black', 1, 1), 
                        Pawn('black', 1, 2), Pawn('black', 1, 3),
                        Pawn('black', 1, 4), Pawn('black', 1, 5),
                        Pawn('black', 1, 6), Pawn('black', 1, 7),
                        King('black', 0, 4), Bishop('black', 0, 2), 
                        Bishop('black', 0, 5), Knight('black', 0, 1), 
                        Knight('black', 0, 6), Tower('black', 0, 0), 
                        Tower('black', 0, 7), Queen('black', 0, 3)]

chess_table = Table()
chess_table.create()

player1 = Player1('Isidro')
player2 = Player2('Yoliber')

player1.insert_pieces(chess_table)
player2.insert_pieces(chess_table)

index = 0
for row in chess_table.c_table:
    pieces = ''
    for box in row:
        piece = box.piece_in_self
        if piece == None:
            pieces+= '[ ]'
        elif isinstance(piece, Tower) and piece.color == 'white':
            pieces+= '[T]'
        elif isinstance(piece, Knight) and piece.color == 'white':
            pieces+= '[H]'
        elif isinstance(piece, Bishop) and piece.color == 'white':
            pieces+= '[B]'
        elif isinstance(piece, Queen) and piece.color == 'white':
            pieces+= '[Q]'
        elif isinstance(piece, King) and piece.color == 'white':
            pieces+= '[K]'
        elif isinstance(piece, Pawn) and piece.color == 'white':
            pieces+= '[P]'
        elif isinstance(piece, Tower) and piece.color == 'black':
            pieces+= '[t]'
        elif isinstance(piece, Knight) and piece.color == 'black':
            pieces+= '[h]'
        elif isinstance(piece, Bishop) and piece.color == 'black':
            pieces+= '[b]'
        elif isinstance(piece, Queen) and piece.color == 'black':
            pieces+= '[q]'
        elif isinstance(piece, King) and piece.color == 'black':
            pieces+= '[k]'
        elif isinstance(piece, Pawn) and piece.color == 'black':
            pieces+= '[p]'
    print(index, pieces)
    index+= 1
print('   0  1  2  3  4  5  6  7')