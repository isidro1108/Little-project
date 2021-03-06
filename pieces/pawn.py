from father_class.piece import Piece
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.tower import Tower
from os import system

class Pawn(Piece):
    # The direction of the pawns depends on their color
    direction = {'white': -1, 'black': 1}

    # Additional features
    def __init__(self, color, p1, p2):
        Piece.__init__(self, color, p1, p2)
        self.value = 1
        self.dir = self.direction[self.color] # <--
        self.movements = [(self.dir, 0), (2 * self.dir, 0)]
        self.c_movements = [(self.dir, -1), (self.dir, 1)]
        self.p_step_capture = False # <--
    
    # Indicates if a movement is within the pawn capture movements
    def __move_in_c_movements(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) in self.c_movements

    # Check if the movement made by the pawn has been two steps
    def __is_two_step(self, p1, p2):
        return (p1 - self.p1, p2 - self.p2) == (2 * self.dir, 0)

    # Set the pawn's control in the boxes
    def set_control(self, table):
        for movement in self.c_movements: # <-- c_movements
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                table.c_table[p1][p2].controlled_by.append((type(self), self.color))
                self.controlled_boxes.append((p1, p2))
    
    # Quit the setted control
    def quit_control(self, table):
        for movement in self.c_movements: # <-- c_movements
            p1, p2 = self.p1 + movement[0], self.p2 + movement[1]
            if table.move_is_inside(p1, p2):
                table.c_table[p1][p2].controlled_by.remove((type(self), self.color))
        self.controlled_boxes = []
    
    # Change the pawn's position
    def change_position(self, table, p1, p2):
        self.quit_control(table)
        self.p1, self.p2 = p1, p2
        self.set_control(table)
    
    # The pawn's movement patterns are the most exceptional
    def move(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.move_in_movements(p1, p2) and destiny.is_available():
                if self.__is_two_step(p1, p2) and not table.c_table[p1 - self.dir][p2].is_available():
                    table.alert = '\nThe pawn cannot jump over another piece'
                    return False
                if self.__is_two_step(p1, p2):
                    self.p_step_capture = True
                else:
                    self.p_step_capture = False
                table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                self.change_position(table, p1, p2)
                if self.moves == 0:
                    self.movements = [(self.dir, 0)]
                if self.p1 == 0 or self.p1 == 7:
                    self.to_crown(table)
                self.moves+= 1
                return True
            table.alert = '\nInvalid movement'
            return False
        return False

    # Capture another piece with this piece (pawn)
    def capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            if self.__move_in_c_movements(p1, p2) and not destiny.is_available():
                f_piece = table.c_table[p1][p2].piece_in_self
                if self.is_enemy_piece(f_piece):
                    table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                    f_piece.dead(table)
                    destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
                    self.change_position(table, p1, p2)
                    if self.p1 == 0 or self.p1 == 7:
                        self.to_crown(table)
                    self.moves+= 1
                    return True
                table.alert = '\nThis is not a enemy piece'
                return False
            table.alert = '\nInvalid movement or there is no piece to capture'
            return False
        return False
    
    # Do the step capture
    def step_capture(self, table, p1, p2):
        if table.move_is_inside(p1, p2):
            destiny = table.c_table[p1][p2]
            c_destiny = table.c_table[p1 - self.dir][p2]
            f_piece = table.c_table[p1 - self.dir][p2].piece_in_self
            if self.__move_in_c_movements(p1, p2) and destiny.is_available() and not c_destiny.is_available():
                if self.is_enemy_piece(f_piece) and f_piece.p_step_capture:
                    table.movement_log.append([(self.p1, self.p2), (p1, p2)])
                    f_piece.dead(table)
                    c_destiny.piece_in_self, destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = None, self, None
                    self.change_position(table, p1, p2)
                    self.moves+= 1
                    return True
                table.alert = '\nThis is not a enemy piece or cannot be captured at step'
                return False
            table.alert = '\nInvalid movement or there is no piece to capture'
            return False
        return False

    # Crown method of the pawn
    def to_crown(self, table):
        system('cls')
        print('\nWhat piece do you want?')
        print('\n1.Queen  2.Tower  3.Bishop  4.Knight')
        op = input('Choose an option:')
        if op == '1':
            crown_piece = Queen(self.color, self.p1, self.p2)
        elif op == '2':
            crown_piece = Tower(self.color, self.p1, self.p2)
        elif op == '3':
            crown_piece = Bishop(self.color, self.p1, self.p2)
        elif op == '4':
            crown_piece = Knight(self.color, self.p1, self.p2)
        else:
            crown_piece = Queen(self.color, self.p1, self.p2)
        p1, p2 = self.p1, self.p2
        table.c_table[p1][p2].piece_in_self = crown_piece
        table.c_table[p1][p2].piece_in_self.g_all_movements()
        table.c_table[p1][p2].piece_in_self.set_control(table)

    # Reverse the last move made
    def revert_move(self, table):
        last_p1, last_p2 = table.movement_log[-1][0][0], table.movement_log[-1][0][1]
        destiny = table.c_table[last_p1][last_p2]
        destiny.piece_in_self, table.c_table[self.p1][self.p2].piece_in_self = self, None
        self.change_position(table, last_p1, last_p2)
        if self.moves == 1:
            self.movements = [(self.dir, 0), (2 * self.dir, 0)]
        else:
            self.movements = [(self.dir, 0)]
        table.movement_log.pop()
        self.moves-= 1

    # The movement is reversed and the captured piece is restored
    def revert_capture(self, table):
        self.revert_move(table)
        table.restore_piece()
