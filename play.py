#!/usr/bin/env python

import moves

def create_board():
    board = [["."] * 8 for _ in range(8)]
    board[0] = ["r", "k", "b", "q", "x", "b", "k", "r"]
    board[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]
    board[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]
    board[7] = ["R", "K", "B", "Q", "X", "B", "K", "R"]

    return board


def get_request():
    fr = input("what piece do you wish to move? ")
    to = input("whereto do you wish to move it? ")

    if fr == to:
        raise Exception("You cannot move to the same tile.")

    # Position conversion to matrix indices
    letter_to_index = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, "f":5, 'g':6, 'h':7}
    number_to_index = {'8':0, '7':1, '6':2, '5':3, '4':4, "3":5, '2':6, '1':7}

    fr = (letter_to_index[fr[0]], number_to_index[fr[1]])
    to = (letter_to_index[to[0]], number_to_index[to[1]])

    return fr, to


def check_validity(M, piece):
    return M.p() if piece == 'p' else print('nah')

def play(board, fr, to, piece):

    M = moves.Moves(board, fr, to, "b", 1)

    if check_validity(M, piece.lower()):
        print("HALLELOO")


    return board

def main():
    board = create_board()
    fr, to = get_request()
    piece = board[fr[1]][fr[0]] # reversed indexing because of matrix

    # while not checkmate():
    play(board, fr, to, piece)

main()
