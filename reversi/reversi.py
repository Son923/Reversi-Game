from ast import literal_eval as eval
import sys


board_size = 9
player = 'B'
BLACK = 'B'
WHITE = 'W'
EMPTY = '.'
offsets = (((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
            (-1, 1)))
# tuple of 8 position around checkpoint


def inverse(piece):
    return BLACK if piece is WHITE else WHITE


def create_board():  # create begining board
    board = [[EMPTY for x in range(9)] for x in range(9)]

    board[4][4] = WHITE
    board[5][5] = WHITE
    board[4][5] = BLACK
    board[5][4] = BLACK

    # for test
    # board[7][7] = WHITE
    # board[6][7] = BLACK
    # board[5][7] = WHITE

    board[0] = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    board[1][0] = '1'
    board[2][0] = '2'
    board[3][0] = '3'
    board[4][0] = '4'
    board[5][0] = '5'
    board[6][0] = '6'
    board[7][0] = '7'
    board[8][0] = '8'
    return board


def game_loop(board, piece):  # Print cur board+valid move+exe move if valid
    # print board
    for row in range(len(board)):
        print(*board[row], sep=' ')
    '\n'
    print(print_valid_move(board, piece) , end ='\n')
    while(True):
        try:
            # change alp to num
            move = []
            if piece == BLACK:
                player = 'B'
            else:
                player = 'W'
            # INPUT
            inputMove = input("Player " + player + ": ")
            errorMove = inputMove
            if (inputMove[0] not in 'abcdefgh' or inputMove[1]
                    not in '12345678' or len(inputMove) > 2):
                raise AssertionError
            else:
                inputMove = inputMove.replace('a', '1')
                inputMove = inputMove.replace('b', '2')
                inputMove = inputMove.replace('c', '3')
                inputMove = inputMove.replace('d', '4')
                inputMove = inputMove.replace('e', '5')
                inputMove = inputMove.replace('f', '6')
                inputMove = inputMove.replace('g', '7')
                inputMove = inputMove.replace('h', '8')
                move.append(int(inputMove[1]))  # change input to (row, col)
                move.append(int(inputMove[0]))  # change input to (row, col)

                # x,y -> y,x (easier to use)
                if is_valid_move(board, piece, move):
                    place_piece(board, piece, move)
                    return
                else:
                    raise AssertionError
        except ((TypeError, ValueError, IndexError,
                SyntaxError, AssertionError)):
            #   ------------------bad  input------------------  ---bad move---
            print(errorMove, ': Invalid choice')
            print(print_valid_move(board, piece), end = '\n')
            sys.exit()


def is_valid_move(board, piece, move):  # check if move is valid, return bool
    if board[move[0]][move[1]] is not EMPTY:
        return False
    for offset in offsets:
        check = [move[0] + offset[0], move[1] + offset[1]]
        while (0 <= check[0] < board_size - 1 and 0 <= check[1] < 8
                and board[check[0]][check[1]] is inverse(piece)):
            check[0] += offset[0]
            check[1] += offset[1]
            if board[check[0]][check[1]] is piece:
                return True
    return False


def place_piece(board, piece, move):  # Execute move and flip
    board[move[0]][move[1]] = piece
    for offset in offsets:
        check = [move[0]+offset[0], move[1]+offset[1]]
        while 0 <= check[0] < board_size and 0 <= check[1] < board_size:
            if board[check[0]][check[1]] is EMPTY:
                break
            if board[check[0]][check[1]] is piece:
                flip(board, piece, move, offset)
                break
            check[0] += offset[0]
            check[1] += offset[1]
    return


def flip(board, piece, move, offset):  # flip inverse piece in middle
    check = [move[0]+offset[0], move[1]+offset[1]]
    while(board[check[0]][check[1]] is inverse(piece)):
        board[check[0]][check[1]] = piece
        check[0] += offset[0]
        check[1] += offset[1]
    return


def has_valid_move(board, piece):  # check if Player has move, return bool
    for y in range(board_size):
        for x in range(board_size):
            if is_valid_move(board, piece, (y, x)):
                return True
    return False


def print_valid_move(board, piece):  # print valid move
    # listValidmove = []
    string = 'abcdefgh'
    validchoice = ''
    for y in range(board_size):
        for x in range(board_size):
            if is_valid_move(board, piece, (x, y)):
                validchoice = validchoice + string[y - 1] + str(x) + ' '
    if validchoice is None:
        return 'Player ' + piece + 'cannot play.'
    else:
        return "Valid choices: " + validchoice


def main():
    board = create_board()
    piece = BLACK
    while has_valid_move(board, piece):  # check if B has move
        game_loop(board, piece)
        if has_valid_move(board, inverse(piece)):  # check if W has move
            piece = inverse(piece)  # turn piece to W
        else:  # If W dont have move
            # print board
            for row in range(len(board)):
                print(*board[row], sep=' ')
            '\n'
            print("Player", inverse(piece), "cannot play.")  # W can not play
            # piece is still B
    # print board
    for row in range(len(board)):
        print(*board[row], sep=' ')
    '\n'
    print("Player", piece, "cannot play.")
    black, white = 0, 0  # set ori score
    # score
    for row in board:
        for token in row:
            if token is WHITE:
                white += 1
            if token is BLACK:
                black += 1
    print('End of the game. W: {}, B: {}'.format(white, black))
    if black == white:
        return "Draw."
    else:
        # print()
        if black > white:
            return 'B wins.'
        else:
            return 'W wins.'


if __name__ == '__main__':
    main()
