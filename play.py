#!/usr/bin/env python
from itertools import product

def create_board():
    board = [["."] * 8 for _ in range(8)]
    board[0] = ["r", "k", "b", "q", "k", "b", "k", "r"]
    board[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]
    board[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]
    board[7] = ["R", "K", "B", "Q", "K", "B", "K", "R"]
    return board

index_to_letter = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, "f":5, 'g':6, 'h':7}
number_to_index = {'8':0, '7':1, '6':2, '5':3, '4':4, "3":5, '2':6, '1':7}

class Moves(object):

    def __init__(self, board, fr, to, player):
        self.board = board
        self.fr_x = index_to_letter[fr[0]]
        self.fr_y = number_to_index[fr[1]]
        self.to_x = index_to_letter[to[0]]
        self.to_y = number_to_index[to[1]]
        self.piece = board[self.fr_x][self.fr_y]
        self.player = player


        if fr == to:
            raise Exception("You cannot move to the same tile.")

        # check if the player is not trying to move a piece onto a tile where
        # they have one of their own pieces
        if player == 'w':
            if board[self.to_y][self.to_x].isupper():
                raise Exception("Invalid move, try again.")
        else:
            if board[self.to_y][self.to_x].islower():
                raise Exception("Invalid move, try again.")


    def r(self):
        """Checks whether the move is valid if the piece is a rook"""

        if self.fr_y == self.to_y:                      # horizontal move
            if self.fr_x < self.to_x:                   # move right
                for i in range(self.fr_x+1, self.to_x):
                    if self.board[self.fr_y][i] is not ".":
                        return False
            else:                                       # move left
                for i in range(self.fr_x-1, self.to_x, -1):
                    if self.board[self.fr_y][i] is not ".":
                        return False

        elif self.fr_x == self.to_x:                    # vertical move
            if self.fr_y < self.to_y:                   # move down
                for i in range(self.fr_y+1, self.to_y):
                    if self.board[i][self.fr_x] is not ".":
                        return False
            else:                                       # move up
                for i in range(self.fr_y-1, self.to_y, -1):
                    if self.board[i][self.fr_x] is not ".":
                        return False

        else: #not a valid tower move
            return False

        return True


    def k(self):
        """Checks whether the move is valid if the piece is a knight"""
        x, y = self.fr_x, self.fr_y
        moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2,x+2], [y-1,y+1]))
        moves = [(x,y) for x,y in moves if 0 <= x < 8 and 0 <= y < 8]

        return (self.to_x, self.to_y) in moves

    def b(self):
        x, y = self.x, self.y

        for i in range(8):
            for y in range(8):
                moves_up = [x]

        return(dia_1)

M = Moves(create_board(), "b1", "d2", "w")

print(M.k())
