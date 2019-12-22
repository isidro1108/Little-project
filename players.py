from table_and_box.table import Table
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

    def is_my_piece(self, piece):
        return piece.color == self.pieces[-1].color

    def move(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        if self.is_my_piece(piece):
            piece.move(table, pd1, pd2)
            piece.update(table)
        else:
            print('Esta no es tu pieza')
    
    def capture(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        if self.is_my_piece(piece):
            piece.capture(table, pd1, pd2)
            piece.update(table)
        else:
            print('Esta no es tu pieza')

    def step_capture(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        if isinstance(piece, Pawn):
            if self.is_my_piece(piece):
                piece.step_capture(table, pd1, pd2)
                piece.update(table)
            else:
                print('Esta no es tu pieza')
        else:
            print('Esta pieza no es un peón')
    
    def castling_to_left(self, table, p1, p2):
        piece = table.c_table[p1][p2].piece_in_self
        if isinstance(piece, King):
            if self.is_my_piece(piece):
                piece.castling_to_left(table)
                piece.update(table)
            else:
                print('Esta no es tu pieza')
        else:
            print('Esta pieza no es un rey')
    
    def castling_to_right(self, table, p1, p2):
        piece = table.c_table[p1][p2].piece_in_self
        if isinstance(piece, King):
            if self.is_my_piece(piece):
                piece.castling_to_right(table)
                piece.update(table)
            else:
                print('Esta no es tu pieza')
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

index = 8
for row in chess_table.c_table:
    pieces = ''
    for box in row:
        piece = box.piece_in_self
        if piece == None:
            pieces+= '[  ]'
        elif isinstance(piece, Tower) and piece.color == 'white':
            pieces+= '[♜ ]'
        elif isinstance(piece, Knight) and piece.color == 'white':
            pieces+= '[♞ ]'
        elif isinstance(piece, Bishop) and piece.color == 'white':
            pieces+= '[♝ ]'
        elif isinstance(piece, Queen) and piece.color == 'white':
            pieces+= '[♛ ]'
        elif isinstance(piece, King) and piece.color == 'white':
            pieces+= '[♚ ]'
        elif isinstance(piece, Pawn) and piece.color == 'white':
            pieces+= '[♟ ]'
        elif isinstance(piece, Tower) and piece.color == 'black':
            pieces+= '[♖ ]'
        elif isinstance(piece, Knight) and piece.color == 'black':
            pieces+= '[♘ ]'
        elif isinstance(piece, Bishop) and piece.color == 'black':
            pieces+= '[♗ ]'
        elif isinstance(piece, Queen) and piece.color == 'black':
            pieces+= '[♕ ]'
        elif isinstance(piece, King) and piece.color == 'black':
            pieces+= '[♔ ]'
        elif isinstance(piece, Pawn) and piece.color == 'black':
            pieces+= '[♙ ]'
    print(index, pieces)
    index-= 1
print('   a   b   c   d   e   f   g   h')