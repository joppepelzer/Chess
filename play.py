#!/usr/bin/env python
from itertools import product

# TODO: Ask for input from player
# TODO: If position is valid, update board
# TODO: Error handling for positions outsde the board

def create_board():
    board = [["."] * 8 for _ in range(8)]
    board[0] = ["r", "k", "b", "q", "x", "b", "k", "r"]
    board[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]
    board[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]
    board[7] = ["R", "K", "B", "Q", "X", "B", "K", "R"]
    return board

index_to_letter = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, "f":5, 'g':6, 'h':7}
number_to_index = {'8':0, '7':1, '6':2, '5':3, '4':4, "3":5, '2':6, '1':7}

class Moves(object):

    def __init__(self, board, fr, to, player, move):
        self.board = board
        self.fr_x = index_to_letter[fr[0]]
        self.fr_y = number_to_index[fr[1]]
        self.to_x = index_to_letter[to[0]]
        self.to_y = number_to_index[to[1]]
        self.piece = board[self.fr_x][self.fr_y]
        self.player = player
        self.move = move

        if fr == to:
            raise Exception("You cannot move to the same tile.")

        # check if the player is not trying to move a piece onto a tile where
        # they have one of their own pieces
        if player == 'w':
            if board[self.to_y][self.to_x].isupper():
                raise Exception("You cannot move onto yourself!")
        else:
            if board[self.to_y][self.to_x].islower():
                raise Exception("You cannot move onto yourself!")


    def rook_horizontal(self, direction):
        for i in direction:
            if self.board[self.fr_y][i] is not ".":
                return False

    def rook_vertical(self, direction):
        for i in direction:
            if self.board[i][self.fr_x] is not ".":
                return False

    def r(self):
        """Checks whether the move is valid if the piece is a rook"""

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
        list of all the possible moves, and then filters out the ones that are
        of the board."""

        x, y = self.fr_x, self.fr_y
        moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2,x+2], [y-1,y+1]))
        # valid_moves = [(x,y) for x,y in moves if 0 <= x < 8 and 0 <= y < 8]

        return (self.to_x, self.to_y) in moves


    def b(self):
        """Checks whether the move is valid if the piece is a bishop. Makes a
        list of all the possible moves, and then filters out the ones that are
        of the board. """
        # TODO: build in collision detection

        x, y = self.fr_x, self.fr_y
        moves = []
        for i in range(1, 8): # 0 is its own position
            moves += list(product([x-i, x+i], [y-i, y+i]))
        # valid_moves = [(x,y) for x,y in moves if 0 <= x < 8 and 0 <= y < 8]

        return (self.to_x, self.to_y) in moves


    def q(self):
        """If horizontal or vertical, follows rook, else bishop"""
        return r() if self.fr_y == self.to_y or self.fr_x == self.to_x else b()


    def x(self):
        """Checks whether the move is valid if the piece is a king. Makes a
        list of all the possible moves, and then filters out the ones that are
        off the board. """

        x, y = self.fr_x, self.fr_y
        moves = list(product([x, x-1, x+1], [y, y-1, y+1]))
        # valid_moves = [(x,y) for x,y in moves if 0 <= x < 8 and 0 <= y < 8]

        return (self.to_x, self.to_y) in moves


    def p(self):
        x, y = self.fr_x, self.fr_y

        moves = []

        if self.board[y-1][x] is '.':
            moves.append((x, y-1))

        if self.board[y-1][x-1] is not '.':
            moves.append((x-1, y-1))

        if self.board[y-1][x+1] is not '.':
            moves.append((x+1, y-1))

        if self.move == '0' or '1':
            moves.append((x, y-2))

        return (self.to_x, self.to_y) in moves


M = Moves(create_board(), "a6", "f6", "w", 1)



print(M.r())
