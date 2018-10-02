from itertools import product

# TODO: Ask for input from player
# TODO: If position is valid, update board
# TODO: Error handling for positions outsde the board

"""
Main check whether the requested move is valid. Asks for the updated board, the
start position of the requested piece, and the end position. Registers what
player is at play, and what move in the game we are at.
"""

class Moves(object):

    def __init__(self, board, fr, to, player, move_count):
        self.board = board
        self.fr_x = fr[0]
        self.fr_y = fr[1]
        self.to_x = to[0]
        self.to_y = to[1]
        self.player = player
        self.move_count = move_count

        self.pieces = {i: i[0] if player == 'w' else i[0].upper()
            for i in ['rook','knight', 'bishop', 'queen','king', 'pawn']}

        if board[self.to_y][self.to_x] in self.pieces.values():
            raise Exception("You cannot move onto yourself!")

    ### HELPER FUNCTIONS ###

    def rook_horizontal(self, direction):
        for i in direction:
            if self.board[self.fr_y][i] is not ".":
                return False

    def rook_vertical(self, direction):
        for i in direction:
            if self.board[i][self.fr_x] is not ".":
                return False

    def bishop_moves(self, direction, moves):
        """Checks all bishop moves that don't collide"""
        for i in range(1, 8):
            new_x = self.fr_x + direction[0] * i
            new_y = self.fr_y + direction[1] * i
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if self.board[new_y][new_x] is '.':
                    moves.append((new_x, new_y))
                if self.board[new_y][new_x] not in self.pieces.values():
                    moves.append((new_x, new_y))
                    break
            else:
                break

    def check_rook(self, d): # Check if desired rook is in starting position
        return self.board[self.fr_y][self.fr_x+d] is self.pieces['rook']

    def no_castling_block(self, d): # Check if no pieces between king & castle
        for x in range(self.fr_x+d, self.to_x, d):
            if self.board[self.fr_y][x] is not '.':
                return False
        return True

    def castling(self, moves): # Check if castling is a valid move at the moment
        if self.to_x > self.fr_x:       # castling kingside
            if self.check_rook(3) and self.no_castling_block(1):
                moves.append((self.fr_x+2, self.fr_y))
        else:                           # castling queenside
            if self.check_rook(-4) and self.no_castling_block(-1):
                moves.append((self.fr_x-2, self.fr_y))

    ### FUNCTIONS PER PIECE ###

    def r(self):
        """Checks whether the move is valid if the piece is a rook."""

        # lists possible positions for a move in every direction
        right = range(self.fr_x+1, self.to_x)
        left  = range(self.fr_x-1, self.to_x, -1)
        up    = range(self.fr_y-1, self.to_y, -1)
        down  = range(self.fr_y+1, self.to_y)

        if self.fr_y == self.to_y:               # horizontal move
            self.rook_horizontal(right if self.fr_x < self.to_x else left)
        elif self.fr_x == self.to_x:             # vertical move
            self.rook_vertical(down if self.fr_y < self.to_y else up)

        else: #not a valid tower move
            return False

        return True


    def k(self):
        """Checks whether the move is valid if the piece is a knight. Makes a
        list of all the possible moves."""

        x, y = self.fr_x, self.fr_y
        moves = list(product([x-1, x+1], [y-2, y+2])) + list(
                     product([x-2,x+2], [y-1,y+1]))

        return (self.to_x, self.to_y) in moves


    def b(self):
        """Checks whether the move is valid if the piece is a bishop. Makes a
        list of all the possible moves."""

        moves = []
        for direction in list(product([-1, 1], [-1, 1])):
            self.bishop_moves(direction, moves)

        return (self.to_x, self.to_y) in moves


    def q(self):
        """If horizontal or vertical, follows rook, else bishop."""
        return self.r() if self.fr_y == self.to_y or self.fr_x == self.to_x else self.b()


    def x(self):
        """Checks whether the move is valid if the piece is a king. Makes a
        list of all the possible moves. Also checks castling possibilities."""

        x, y = self.fr_x, self.fr_y
        moves = list(product([x, x-1, x+1], [y, y-1, y+1]))

        if (self.to_x, self.to_y) == (x-2, y) or (x+2, y):
            self.castling(moves)

        return (self.to_x, self.to_y) in moves


    def p(self):
        """Checks wheters the move is valid if the piece is a pawn. Checks all
        cases separately, and ultimately if it's the first turn, since a pawn
        can then move two tiles ahead."""

        x, y = self.fr_x, self.fr_y
        moves = []
        d = -1 if self.player == 'w' else 1

        if self.board[y+d][x] is '.':
            moves.append((x, y+d))

        if self.board[y+d][x-1] is not '.':
            moves.append((x-1, y+d))

        if self.board[y+d][x+1] is not '.':
            moves.append((x+1, y+d))

        if (self.move_count == '0' or '1') and (self.board[y+d*2][x] is '.'):
            moves.append((x, y+d*2))

        return (self.to_x, self.to_y) in moves
