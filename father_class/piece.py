# This is the parent class of all the pieces 
class Piece:
    # piece's features
    def __init__(self, color, p1, p2):
        self.color = color
        self.p1 = p1
        self.p2 = p2
        self.value = None
        self.alive = True
        self.moves = 0
        self.movements = []
        self.controlled_boxes = [] 

    # This method determines if a movement is within the movement patterns of a piece
    def move_in_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.movements

    # Overwritten method (explanation in mpiece.py)
    def g_all_movements(self):
        pass
    
    # Establishes control of the piece over their respective boxes
    def set_control(self, table):
        for movement in self.movements:
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                table.c_table[p1][p2].controlled_by.append((type(self), self.color))
                self.controlled_boxes.append((p1, p2))
    
    # Revert the set_control action
    def quit_control(self, table):
        for movement in self.movements:
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                if (p1, p2) in self.controlled_boxes:
                    table.c_table[p1][p2].controlled_by.remove((type(self), self.color))
        self.controlled_boxes = []
    
    # Remove the control of the piece, change its position and then set the new control
    def change_position(self, table, p1, p2):
        self.quit_control(table)
        self.p1, self.p2 = p1, p2
        self.set_control(table)

    # Check if a piece belongs to the other player
    def is_enemy_piece(self, piece):
        return isinstance(piece, Piece) and piece.color != self.color

    # Method that performs the movement of the piece
    def move(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and destiny.is_available():
                table.movement_log.append([(self.p1, self.p2), (p1, p2)]) # Record the movement if it is valid
                destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                self.change_position(table, p1, p2)
                self.moves+= 1
                return True
            table.alert = '\nInvalid movement'
            return False
        return False

    # Method that executes the capture action of the piece
    def capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and not destiny.is_available():
                f_piece = table.c_table[p1][p2].piece_in_self
                if self.is_enemy_piece(f_piece):
                    table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                    f_piece.dead(table)
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    self.change_position(table, p1, p2)
                    self.moves+= 1
                    return True
                table.alert = '\nThis is not a enemy piece'
                return False
            table.alert = '\nInvalid movement or there is no piece to capture'
            return False
        return False
    
    # Remove the piece from the board and enter it in a repository and remove all the controlled boxes
    def dead(self, table):
        self.alive = False
        table.repository.append(self)
        for pos in self.controlled_boxes:
            table.c_table[pos[0]][pos[1]].controlled_by.remove((type(self), self.color))
        self.controlled_boxes = []

    # Reverse the move made and remove it from the movement log
    def revert_move(self, table):
        last_p1, last_p2 = table.movement_log[-1][0][0], table.movement_log[-1][0][1]
        table.c_table[last_p1][last_p2].piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
        self.change_position(table, last_p1, last_p2)
        table.movement_log.pop()
        self.moves-= 1

    # Reverse the capture made and remove it from the movement log
    def revert_capture(self, table):
        last_p1, last_p2 = table.movement_log[-1][0][0], table.movement_log[-1][0][1]
        table.c_table[last_p1][last_p2].piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
        self.change_position(table, last_p1, last_p2)
        table.restore_piece()
        table.movement_log.pop()
        self.moves-= 1
