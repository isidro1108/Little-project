from players import Player1, Player2, King, Queen, Bishop, Knight, Tower, Pawn, Table

chess_table = Table()
chess_table.create()

player1 = Player1('Chester')
player2 = Player2('Michael')

player1.insert_pieces(chess_table)
player2.insert_pieces(chess_table)

player1.move(chess_table, 6, 3, 4, 3)
player1.move(chess_table, 7, 1, 5, 2)
player1.move(chess_table, 7, 2, 4, 5)
player1.move(chess_table, 7, 3, 5, 3)
player2.move(chess_table, 1, 4, 3, 4)
player2.move(chess_table, 0, 3, 3, 6)
player2.capture(chess_table, 3, 6, 4, 5)
# player2.move(chess_table, 4, 5, 6, 3)
player2.capture(chess_table, 4, 5, 6, 5)
player1.castling_to_left(chess_table)

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