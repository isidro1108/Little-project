from players import Player1, Player2, King, Queen, Bishop, Knight, Tower, Pawn, Table
from os import system

# This class contains the game events
class Game:
    # Game Attributes
    def __init__(self):
        self.chess_table = Table()
        self.col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        self.player1 = None
        self.player2 = None
        self.possible_positions = []

    # Create the board, enter the players and they insert their pieces
    def intro(self):
        self.chess_table.create()
        while True:
            system('cls')
            print('\n**************************Chess Game**************************\n')
            print('Players\n')
            if self.chess_table.alert != '':
                print(self.chess_table.alert)
            name_p1 = input('Insert the name of the white player:')
            name_p2 = input('Insert the name of the black player:')
            self.player1 = Player1(name_p1)
            self.player2 = Player2(name_p2)
            is_good_length = len(name_p1) <= 8 and len(name_p2) <= 8
            are_letters = self.__valid_input(name_p1) and self.__valid_input(name_p2) 
            if is_good_length and are_letters:
                break
            self.chess_table.alert = 'Only 8 characters or at least one, neither should they be numbers\n'
        self.chess_table.alert = ''
        self.player1.insert_pieces(self.chess_table)
        self.player2.insert_pieces(self.chess_table)
        self.__get_possible_positions()
    
    # Makes a list of valid entries for positions
    def __get_possible_positions(self):
        for c in range(ord('a'), ord('h') + 1):
            for r in range(1, 9):
                self.possible_positions.append(chr(c) + str(r))

    # Indicate if the position is valid
    def __valid_position(self, p):
        return p in self.possible_positions

    # Indicate if the input name is valid
    def __valid_input(self, entry):
        for char in entry:
            is_number = ord(char) >= ord('0') and ord(char) <= ord('9')
            if is_number:
                return False
        return entry != ''

    # Disable the ability to capture a pawn in step
    def off_step_capture(self, player):
        for pawn in player.pieces[:8]:
            pawn.p_step_capture = False

    # The following methods convert game coordinates 
    # to matrix coordinates and execute player movement methods
    def __move(self, player):
        p = input('Insert the position of the piece you want to move:')
        if not self.__valid_position(p):
            self.chess_table.alert = '\nInvalid input'
            return False
        pd = input('Where do you want to move:')
        if not self.__valid_position(pd):
            self.chess_table.alert = '\nInvalid input'
            return False
        # For example
        p1, p2 = 8 - int(p[1]), self.col[p[0]] # <--
        pd1, pd2 = 8 - int(pd[1]), self.col[pd[0]] # <--
        if self.chess_table.c_table[p1][p2].piece_in_self == None:
            self.chess_table.alert = 'This box is empty'
            return False
        move = player.move(self.chess_table, p1, p2, pd1, pd2)
        return move
        

    # Capture method
    def __capture(self, player):
        p = input('Insert the position of the piece with which you want to capture:')
        if not self.__valid_position(p):
            self.chess_table.alert = '\nInvalid input'
            return False
        pd = input('Where do you want to capture:')
        if not self.__valid_position(pd):
            self.chess_table.alert = '\nInvalid input'
            return False
        p1, p2 = 8 - int(p[1]), self.col[p[0]]
        pd1, pd2 = 8 - int(pd[1]), self.col[pd[0]]
        if self.chess_table.c_table[p1][p2].piece_in_self == None:
            self.chess_table.alert = 'This box is empty'
            return False
        move = player.capture(self.chess_table, p1, p2, pd1, pd2)
        return move

    # Step capture method
    def __step_capture(self, player):
        p = input('Insert the position of the piece with which you want to capture:')
        if not self.__valid_position(p):
            self.chess_table.alert = '\nInvalid input'
            return False
        pd = input('Where do you want to capture:')
        if not self.__valid_position(pd):
            self.chess_table.alert = '\nInvalid input'
            return False
        p1, p2 = 8 - int(p[1]), self.col[p[0]]
        pd1, pd2 = 8 - int(pd[1]), self.col[pd[0]]
        if self.chess_table.c_table[p1][p2].piece_in_self == None:
            self.chess_table.alert = 'This box is empty'
            return False
        move = player.step_capture(self.chess_table, p1, p2, pd1, pd2)
        return move

    # Perform left castling
    def __castling_to_left(self, player):
        move = player.castling_to_left(self.chess_table)
        return move

    # Perform right castling
    def __castling_to_right(self, player):
        move = player.castling_to_right(self.chess_table)
        return move

    # Print a set of strings that show the instances of empty part and boxes on the board
    def __print_chess_table(self, table):
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
            print(index, pieces)
            index-= 1
        print('   a   b   c   d   e   f   g   h')

    # Start game events
    def init_game(self):
        turn = 1
        while True:
            if turn % 2 != 0:
                system('cls')
                player = self.player1
                ad_player = self.player2
                if player.pieces[8].in_check:
                    player.verify_checkmate(self.chess_table)
                    if player.pieces[8].in_checkmate:
                        break
                    self.chess_table.check_alert = '\nThe white king is in check'
                print("White's turn ({})\n".format(player.name))
            else:
                system('cls')
                player = self.player2
                ad_player = self.player1
                if player.pieces[8].in_check:
                    player.verify_checkmate(self.chess_table)
                    if player.pieces[8].in_checkmate:
                        break
                    self.chess_table.check_alert = '\nThe black king is in check'
                print("Black's turn ({})\n".format(player.name))

            self.__print_chess_table(self.chess_table)
            print(self.chess_table.check_alert)
            self.chess_table.check_alert = ''
            print('\n1. move  2. Capture  3. Step capture  4. Castling to left  5. Castling to right  6. Exit')
            op = input('Choose an option:')
            if op == '1':
                if self.__move(player):
                    self.off_step_capture(ad_player)
                    turn+= 1
                else:
                    input(self.chess_table.alert)
            elif op == '2':
                if self.__capture(player):
                    self.off_step_capture(ad_player)
                    turn+= 1
                else:
                    input(self.chess_table.alert)
            elif op == '3':
                if self.__step_capture(player):
                    turn+= 1
                else:
                    input(self.chess_table.alert)
            elif op == '4':
                if self.__castling_to_left(player):
                    self.off_step_capture(ad_player)
                    turn+= 1
                else:
                    input(self.chess_table.alert)
            elif op == '5':
                if self.__castling_to_right(player):
                    self.off_step_capture(ad_player)
                    turn+= 1
                else:
                    input(self.chess_table.alert)
            elif op == '6':
                system('cls')
                exit()
            else:
                self.chess_table.alert = '\nIncorrect option'
                input(self.chess_table.alert)
        # Check who won
        if player == self.player1:
            self.__print_chess_table(self.chess_table)
            print('\n**************************Check mate, Black wins**************************')
        else:
            self.__print_chess_table(self.chess_table)
            print('\n**************************Check mate, White wins**************************')

chess_game = Game()
chess_game.intro()
chess_game.init_game()
