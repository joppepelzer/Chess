#!/usr/bin/env python

import moves

def create_board():
    board = [["."] * 8 for _ in range(8)]
    board[0] = ["r", "k", "b", "q", "x", "b", "k", "r"]
    board[1] = ["p", "p", "p", "p", "p", "p", "p", "p"]
    board[6] = ["P", "P", "P", "P", "P", "P", "P", "P"]
    board[7] = ["R", "K", "B", "Q", "X", "B", "K", "R"]

    return board


def get_request(colour, move_count):

    if move_count > 0:
        print("{}, it's your turn. ".format(colour))

    fr = input("What piece do you wish to move? ").lower()
    to = input("Whereto do you wish to move it? ").lower()

    # Position conversion to matrix indices
    letter_to_index = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, "f":5, 'g':6, 'h':7}
    number_to_index = {'8':0, '7':1, '6':2, '5':3, '4':4, "3":5, '2':6, '1':7}

    fr = (letter_to_index[fr[0]], number_to_index[fr[1]])
    to = (letter_to_index[to[0]], number_to_index[to[1]])

    return fr, to


def check_validity(M, piece):

    pieces   = ['p', 'r', 'k', 'b', 'q', 'x']
    function = [M.p(), M.r(), M.k(), M.b(), M.q(), M.x()]

    return function[pieces.index(piece)]


def checkmate():
    pass


def print_board(board):
    print('')
    for row in board:
        print(row)
    print('')


def play(board, fr, to, colour, move_count):

    M = moves.Moves(board, fr, to, colour, move_count)
    piece = board[fr[1]][fr[0]] # reversed indexing because of matrix

    if check_validity(M, piece.lower()):
         board[to[1]][to[0]] = board[fr[1]][fr[0]]
         board[fr[1]][fr[0]] = '.'
         kicked_off          = board[to[1]][to[0]]
    else:
        return False

    checkmate()
    print_board(board)

    return board


def main():
    board = create_board()
    print_board(board)
    move_count = 0
    off_board = []

    print("\nWhite, you play with capital letters, you can start.")

    while move_count < 10:
        colour = 'White' if move_count % 2 == 0 else 'Black'

        while True:
            fr, to = get_request(colour, move_count)
            pieces = {i: i[0] if colour == 'White' else i[0].upper()
                for i in ['rook', 'knight', 'bishop', 'queen', 'king', 'pawn']}

            if board[fr[1]][fr[0]] == '.':
                print("There is no piece at this position, try again!")
                continue

            if board[to[1]][to[0]] in pieces.values():
                print("You cannot move onto yourself, try again!")
                continue

            board = play(board, fr, to, colour, move_count)

            if not board:
                print("That's not a valid move, try again!")
                continue



        # off_board.append(kicked_off)
        move_count += 1


if __name__ == "__main__":
    main()
