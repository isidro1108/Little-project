from players import Player1, Player2, King, Queen, Bishop, Knight, Tower, Pawn, Table
from os import system

class Game:
    def __init__(self):
        self.chess_table = Table()
        self.col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        self.player1 = None
        self.player2 = None

    def intro(self):
        self.chess_table.create()

        system('cls')
        print('\n**************************Chess Game**************************\n')
        print('Players\n ')
        self.player1 = Player1(input('Insert the name of the white player:'))
        self.player2 = Player2(input('Insert the name of the black player:'))

        self.player1.insert_pieces(self.chess_table)
        self.player2.insert_pieces(self.chess_table)

    def __valid_position(self, p):
        positions = []
        for c in range(ord('a'), ord('h') + 1):
            for r in range(1, 9):
                positions.append(chr(c) + str(r))
        return p in positions

    def __move(self, player):
        p = input('Insert the position of the piece you want to move: ')
        pd = input('Where do you want to move: ')
        if self.__valid_position(p) and self.__valid_position(pd):
            p1, p2 = 8 - int(p[1]), self.col[p[0]]
            pd1, pd2 = 8 - int(pd[1]), self.col[pd[0]]
            if self.chess_table.c_table[p1][p2].piece_in_self == None:
                self.chess_table.alert = 'This box is empty'
                return False
            move = player.move(self.chess_table, p1, p2, pd1, pd2)
            return move
        self.chess_table.alert = 'Invalid input'
        return False

    def __capture(self, player):
        p = input('Insert the position of the piece with which you want to capture: ')
        pd = input('Where do you want to capture: ')
        if self.__valid_position(p) and self.__valid_position(pd):
            p1, p2 = 8 - int(p[1]), self.col[p[0]]
            pd1, pd2 = 8 - int(pd[1]), self.col[pd[0]]
            if self.chess_table.c_table[p1][p2].piece_in_self == None:
                self.chess_table.alert = 'This box is empty'
                return False
            move = player.capture(self.chess_table, p1, p2, pd1, pd2)
            return move
        self.chess_table.alert = 'Invalid input'
        return False

    def __step_capture(self, player):
        p = input('Insert the position of the piece with which you want to capture: ')
        pd = input('Where do you want to capture: ')
        if self.__valid_position(p) and self.__valid_position(pd):
            p1, p2 = 8 - int(p[1]), self.col[p[0]]
            pd1, pd2 = 8 - int(pd[1]), self.col[pd[0]]
            if self.chess_table.c_table[p1][p2].piece_in_self == None:
                self.chess_table.alert = 'This box is empty'
                return False
            move = player.step_capture(self.chess_table, p1, p2, pd1, pd2)
            return move
        self.chess_table.alert = 'Invalid input'
        return False

    def __castling_to_left(self, player):
        move = player.castling_to_left(self.chess_table)
        return move

    def __castling_to_right(self, player):
        move = player.castling_to_right(self.chess_table)
        return move

    def __print_chess_table(self, table, show_alert= True):
        index = 8
        for row in table.c_table:
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
            if index == 5 and show_alert:
                print(index, pieces, table.alert)
                table.alert = ''
            else:
                print(index, pieces)
            index-= 1
        print('   a   b   c   d   e   f   g   h')

    def init_game(self):    
        turn = 1
        while True:
            if turn % 2 != 0:
                system('cls')
                player = self.player1
                if player.pieces[8].in_check:
                    player.verify_checkmate(self.chess_table)
                    if player.pieces[8].in_checkmate:
                        break
                    self.chess_table.alert = 'White king is in check'
                print("White's turn ({})\n".format(player.name))
            else:
                system('cls')
                player = self.player2
                if player.pieces[8].in_check:
                    player.verify_checkmate(self.chess_table)
                    if player.pieces[8].in_checkmate:
                        break
                    self.chess_table.alert = 'Black king is in check'
                print("Black's turn ({})\n".format(player.name))

            self.__print_chess_table(self.chess_table)
            print('\n1. move  2. Capture  3. Step capture  4. Castling to left  5. Castling to right  6. Exit')
            op = input('Choose an option: ')
            print(op)
            if op == '1':
                if self.__move(player):
                    turn+= 1
            elif op == '2':
                if self.__capture(player):
                    turn+= 1
            elif op == '3':
                if self.__step_capture(player):
                    turn+= 1
            elif op == '4':
                if self.__castling_to_left(player):
                    turn+= 1
            elif op == '5':
                if self.__castling_to_right(player):
                    turn+= 1
            elif op == '6':
                system('cls')
                exit()
            else:
                self.chess_table.alert = 'Incorrect option'

        if player == self.player1:
            self.__print_chess_table(self.chess_table, False)
            print('\n**************************Check mate, Black wins**************************')
        else:
            self.__print_chess_table(self.chess_table, False)
            print('\n**************************Check mate, White wins**************************')

chess_game = Game()
chess_game.intro()
chess_game.init_game()
