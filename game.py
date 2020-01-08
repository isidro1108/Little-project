from players import Player1, Player2, King, Queen, Bishop, Knight, Tower, Pawn, Table

chess_table = Table()
chess_table.create()

player1 = Player1('Chester')
player2 = Player2('Michael')

player1.insert_pieces(chess_table)
player2.insert_pieces(chess_table)

player1.move(chess_table, 6, 4, 4, 4)
player2.move(chess_table, 1, 4, 3, 4)
player1.move(chess_table, 6, 5, 5, 5)
player2.move(chess_table, 0, 3, 4, 7)
# player1.move(chess_table, 7, 4, 6, 4)

# print(chess_table.c_table[7][4].piece_in_self.in_check)
print(player1.pieces[8].in_check)

index = 0
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
    index+= 1
print('   0   1   2   3   4   5   6   7')