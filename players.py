from table_things.table import Table
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
        return piece in self.pieces

    def move(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        if piece != None:
            if piece not in self.pieces and piece.color == self.pieces[-1].color:
                self.pieces.append(piece)
        if self.is_my_piece(piece):
            move = piece.move(table, pd1, pd2)
            table.update()
            if self.pieces[8].in_check and move:
                piece.revert_move(table)
                table.update()
                table.alert = 'The king is in check with this movement'
                return False
            return move
        table.alert = "It isn't your piece"
        return False
    
    def capture(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        if piece != None:
            if piece not in self.pieces and piece.color == self.pieces[-1].color:
                self.pieces.append(piece)
        if self.is_my_piece(piece):
            move = piece.capture(table, pd1, pd2)
            table.update()
            if self.pieces[8].in_check and move:
                piece.revert_capture(table)
                table.update()
                table.alert = 'The king is in check with this movement'
                return False
            return move
        table.alert = "It isn't your piece"
        return False

    def step_capture(self, table, p1, p2, pd1, pd2):
        piece = table.c_table[p1][p2].piece_in_self
        if isinstance(piece, Pawn):
            if self.is_my_piece(piece):
                move = piece.step_capture(table, pd1, pd2)
                table.update()
                if self.pieces[8].in_check and move:
                    piece.revert_capture(table)
                    table.update()
                    table.alert = 'The king is in check with this movement'
                    return False
                return move
            table.alert = "It isn't your piece"
            return False
        table.alert = 'This piece is not a pawn'
        return False
    
    def castling_to_left(self, table):
        p1 = table.pos_kings[self.pieces[0].color][0]
        piece = table.c_table[p1][4].piece_in_self
        if isinstance(piece, King):
            if self.is_my_piece(piece):
                move = piece.castling_to_left(table)
                table.update()
                return move
            table.alert = "It isn't your piece"
            return False
        table.alert = 'This piece is not a king'
        return False
    
    def castling_to_right(self, table):
        p1 = table.pos_kings[self.pieces[0].color][0]
        piece = table.c_table[p1][4].piece_in_self
        if isinstance(piece, King):
            if self.is_my_piece(piece):
                move = piece.castling_to_right(table)
                table.update()
                return move
            table.alert = "It isn't your piece"
            return False
        table.alert = 'This piece is not a king'
        return False

    def verify_checkmate(self, table):
        available_movements = 0
        if self.pieces[8].in_check:
            for piece in self.pieces:
                for movement in piece.movements:
                    p1, p2 = piece.p1 + movement[0], piece.p2 + movement[1]
                    if table.move_is_inside(p1, p2):
                        if self.move(table, piece.p1, piece.p2, p1, p2):
                            if not self.pieces[8].in_check:
                                available_movements+= 1
                                piece.revert_move(table)
                        if self.capture(table, piece.p1, piece.p2, p1, p2):
                            if not self.pieces[8].in_check:
                                available_movements+= 1
                                piece.revert_capture(table)
        self.pieces[8].in_checkmate = available_movements == 0



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