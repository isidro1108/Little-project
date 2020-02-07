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
    p = input('Inserte la posicion de la pieza que desea mover: ')
    pd = input('Donde desea moverse: ')
    if valid_position(p) and valid_position(pd):
        p1, p2 = 8 - int(p[1]), col[p[0]]
        pd1, pd2 = 8 - int(pd[1]), col[pd[0]]
        move = player.move(chess_table, p1, p2, pd1, pd2)
        return move
    return False

def capture(player):
    p = input('Inserte la posicion de la pieza con la que desea capturar: ')
    pd = input('Donde desea capturar: ')
    if valid_position(p) and valid_position(pd):
        p1, p2 = 8 - int(p[1]), col[p[0]]
        pd1, pd2 = 8 - int(pd[1]), col[pd[0]]
        move = player.capture(chess_table, p1, p2, pd1, pd2)
        return move
    return False

def step_capture(player):
    p = input('Inserte la posicion de la pieza con la que desea capturar: ')
    pd = input('Donde desea capturar: ')
    if valid_position(p) and valid_position(pd):
        p1, p2 = 8 - int(p[1]), col[p[0]]
        pd1, pd2 = 8 - int(pd[1]), col[pd[0]]
        move = player.step_capture(chess_table, p1, p2, pd1, pd2)
        return move
    return False

def castling_to_left(player):
    move = player.castling_to_left(chess_table)
    return move

def castling_to_right(player):
    move = player.castling_to_right(chess_table)
    return move

def print_chess_table():
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
    
turn = 1
while True:
    if turn % 2 != 0:
        system('cls')
        player = player1
        print('Turno de las blancas')
        print()
    else:
        system('cls')
        player = player2
        print('Turno de las negras')
        print()

    print_chess_table()
    print()
    print('1. Mover  2. Capturar  3. Capturar al paso  4. Enroque a la izquierda  5. Enroque a la derecha')
    op = input('Elige una opcion: ')
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
        print('Elija la opcion correctamente')
    