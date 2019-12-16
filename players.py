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

class Player1(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.pieces = [King('white', 7, 4), Queen('white', 7, 3),
                        Bishop('white', 7, 2), Bishop('white', 7, 5), 
                        Knight('white', 7, 1), Knight('white', 7, 6),
                        Tower('white', 7, 0), Tower('white', 7, 7), 
                        Pawn('white', 6, 0), Pawn('white', 6, 1), 
                        Pawn('white', 6, 2), Pawn('white', 6, 3),
                        Pawn('white', 6, 4), Pawn('white', 6, 5),
                        Pawn('white', 6, 6), Pawn('white', 6, 7)]

class Player2(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.pieces = [King('black', 0, 4), Queen('black', 0, 3),
                        Bishop('black', 0, 2), Bishop('black', 0, 5), 
                        Knight('black', 0, 1), Knight('black', 0, 6),
                        Tower('black', 0, 0), Tower('black', 0, 7), 
                        Pawn('black', 1, 0), Pawn('black', 1, 1), 
                        Pawn('black', 1, 2), Pawn('black', 1, 3),
                        Pawn('black', 1, 4), Pawn('black', 1, 5),
                        Pawn('black', 1, 6), Pawn('black', 1, 7)]

chess_table = Table()
chess_table.create()

player1 = Player1('Isidro')
player2 = Player2('Yoliber')

player1.insert_pieces(chess_table)
player2.insert_pieces(chess_table)

pawn1 = chess_table.c_table[6][4].piece_in_self
pawn2 = chess_table.c_table[1][4].piece_in_self

pawn2.move(chess_table, 3, 4)
pawn2.move(chess_table, 4, 4)
pawn2.move(chess_table, 5, 4)
pawn1.move(chess_table, 4, 4)