#!/usr/bin/env python

def create_board():
    board = [["."] * 8 for _ in range(8)]
    board[0] = ["r", "k", "b", "q", "k", "b", "k", "r"]
    board[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]
    board[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]
    board[7] = ["R", "K", "B", "Q", "K", "B", "K", "R"]
    return board

index_to_letter = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, "f":5, 'g':6, 'h':7}


class Moves(object):

    def __init__(self, board, fr, to):
        self.board = board
        self.fr_x = index_to_letter[fr[0]]
        self.fr_y = int(fr[1])-1
        self.to_x = index_to_letter[to[0]]
        self.to_y = int(to[1])-1
        self.piece = board[self.fr_x][self.fr_y]

        if fr == to:
            raise Exception("You cannot move to the same tile.")

        if board[self.to_y][self.to_x].islower():
            raise Exception("Invalid move, try again.")


    def r(self):
        """Checks whether the move is valid if the piece is the rook"""

        if self.fr_y == self.to_y: # horizontal move
            if self.fr_x < self.to_x: # move right
                for i in range(self.fr_x, self.to_x+1):
                    print(self.board[self.fr_y][i])
                    if self.board[self.fr_y][i] is not ".":
                        return False
            else: # move left
                for i in range(self.fr_x, self.to_x+1, -1):
                    print(self.board[self.fr_y][i])
                    if self.board[self.fr_y][i] is not ".":
                        return False

        elif self.fr_x == self.to_x: # vertical move
            if self.fr_y < self.to_y: # move down
                for i in range(self.fr_y, self.to_y+1):
                    print(self.board[i][self.fr_x])
                    if self.board[i][self.fr_x] is not ".":
                        return False
            else: # move up
                for i in range(self.fr_y, self.to_y+1, -1):
                    print(self.board[i][self.fr_x])
                    if self.board[i][self.fr_x] is not ".":
                        return False
        else: #not a valid tower move
            return False

        return true

    def k(self):
        x, y = self.x, self.y
        moves = []

        pass

    def b(self):
        x, y = self.x, self.y

        for i in range(8):
            for y in range(8):
                moves_up = [x]

        return(dia_1)

M = Moves(create_board(), "a8", "a4")

print(M.r())
