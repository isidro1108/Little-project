from players import Player1, Player2, King, Queen, Bishop, Knight, Tower, Pawn, Table
from os import system

chess_table = Table()
chess_table.create()

player1 = Player1('Chester')
player2 = Player2('Michael')

player1.insert_pieces(chess_table)
player2.insert_pieces(chess_table)

col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

def valid_position(p):
    positions = []
    for c in range(ord('a'), ord('h') + 1):
        for r in range(1, 9):
            positions.append(chr(c) + str(r))
    return p in positions

def move(player):
    p = input('Insert the position of the piece you want to move: ')
    pd = input('Where do you want to move: ')
    if valid_position(p) and valid_position(pd):
        p1, p2 = 8 - int(p[1]), col[p[0]]
        pd1, pd2 = 8 - int(pd[1]), col[pd[0]]
        if chess_table.c_table[p1][p2].piece_in_self == None:
            chess_table.alert = 'This box is empty'
            return False
        move = player.move(chess_table, p1, p2, pd1, pd2)
        return move
    chess_table.alert = 'Invalid input'
    return False

def capture(player):
    p = input('Insert the position of the piece with which you want to capture: ')
    pd = input('Where do you want to capture: ')
    if valid_position(p) and valid_position(pd):
        p1, p2 = 8 - int(p[1]), col[p[0]]
        pd1, pd2 = 8 - int(pd[1]), col[pd[0]]
        if chess_table.c_table[p1][p2].piece_in_self == None:
            chess_table.alert = 'This box is empty'
            return False
        move = player.capture(chess_table, p1, p2, pd1, pd2)
        return move
    chess_table.alert = 'Invalid input'
    return False

def step_capture(player):
    p = input('Insert the position of the piece with which you want to capture: ')
    pd = input('Where do you want to capture: ')
    if valid_position(p) and valid_position(pd):
        p1, p2 = 8 - int(p[1]), col[p[0]]
        pd1, pd2 = 8 - int(pd[1]), col[pd[0]]
        if chess_table.c_table[p1][p2].piece_in_self == None:
            chess_table.alert = 'This box is empty'
            return False
        move = player.step_capture(chess_table, p1, p2, pd1, pd2)
        return move
    chess_table.alert = 'Invalid input'
    return False

def castling_to_left(player):
    move = player.castling_to_left(chess_table)
    return move

def castling_to_right(player):
    move = player.castling_to_right(chess_table)
    return move

def print_chess_table(table, show_alert= True):
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
    
turn = 1
while True:
    if turn % 2 != 0:
        system('cls')
        player = player1
        if player.pieces[8].in_check:
            player.verify_checkmate(chess_table)
            if player.pieces[8].in_checkmate:
                break
            chess_table.alert = 'White king is in check'
        print("White's turn")
        print()
    else:
        system('cls')
        player = player2
        if player.pieces[8].in_check:
            player.verify_checkmate(chess_table)
            if player.pieces[8].in_checkmate:
                break
            chess_table.alert = 'Black king is in check'
        print("Black's turn")
        print()

    print_chess_table(chess_table)
    print()
    print('1. Move  2. Capture  3. Step capture  4. Castling to left  5. Castling to right')
    op = input('Choose an option: ')
    print(op)
    if op == '1':
        if move(player):
            turn+= 1
    elif op == '2':
        if capture(player):
            turn+= 1
    elif op == '3':
        if step_capture(player):
            turn+= 1
    elif op == '4':
        if castling_to_left(player):
            turn+= 1
    elif op == '5':
        if castling_to_right(player):
            turn+= 1
    else:
        chess_table.alert = 'Incorrect option'

if player == player1:
    print_chess_table(chess_table, False)
    print()
    print('**************************Check mate, Black wins**************************')
else:
    print_chess_table(chess_table, False)
    print()
    print('**************************Check mate, White wins**************************')
    