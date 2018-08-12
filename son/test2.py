from ast import literal_eval as eval

board_size = 8
player = 'A'
BLACK = 'B'
WHITE = 'W'
EMPTY = '.'
offsets = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))

def inverse(piece):
    return BLACK if piece is WHITE else WHITE

def main():
    board = create_board()
    piece = BLACK
    while has_valid_move(board, piece):
        game_loop(board, piece)
        if has_valid_move(board, inverse(piece)):
            piece = inverse(piece)
    print_board(board)
    black, white = 0,0
    for row in board:
        for token in row:
            if token is WHITE: white += 1
            if token is BLACK: black += 1
    if black == white:
        print("It's a tie!")
    else:
        print()
        print('{token} is the winner!' % (BLACK if black>white else WHITE))
    return

def create_board():
    board = [[EMPTY for x in range(9)] for x in range(9)]
    half = board_size//2
    board[half][half] = WHITE
    board[half + 1][half + 1] = WHITE
    board[half][half + 1] = BLACK
    board[half + 1][half] = BLACK
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

def print_board(board):
    for row in range(len(board)):
        print(*board[row], sep=' ')
    return

def game_loop(board, piece):
    print()
    print_board(board)
    print_valid_move(board, piece)
    while(True):
        try:
            # change alp to num
            move = []
            if piece == BLACK:
                player = 'A'
            else:
                player = 'B'
            inputMove = input("Player " + player + ": ")
            errorMove = inputMove
            inputMove = inputMove.replace('a','1')
            inputMove = inputMove.replace('b','2')
            inputMove = inputMove.replace('c','3')
            inputMove = inputMove.replace('d','4')
            inputMove = inputMove.replace('e','5')
            inputMove = inputMove.replace('f','6')
            inputMove = inputMove.replace('g','7')
            inputMove = inputMove.replace('h','8')
            move.append(int(inputMove[1]))  # change input to (row, col)
            move.append(int(inputMove[0]))  # change input to (row, col)

            # x,y -> y,x (easier to use)
            if is_valid_move(board, piece, move):
                place_piece(board, piece, move)
                return
            else:
                raise AssertionError
        except (TypeError, ValueError, IndexError, SyntaxError, AssertionError):
            #   ------------------bad  input------------------  ---bad move---
            print(errorMove, ': Invalid choice')

def is_valid_move(board, piece, move):
    if board[move[0]][move[1]] is not EMPTY: return False
    for offset in offsets:
        check = [move[0]+offset[0], move[1]+offset[1]]
        while 0<=check[0]<board_size-1 and 0<=check[1]<board_size-1 and \
              board[check[0]][check[1]] is inverse(piece):
            check[0] += offset[0]
            check[1] += offset[1]
            if board[check[0]][check[1]] is piece:
                return True
    return False

def place_piece(board, piece, move):
    board[move[0]][move[1]] = piece
    for offset in offsets:
        check = [move[0]+offset[0], move[1]+offset[1]]
        while 0<=check[0]<board_size and 0<=check[1]<board_size:
            if board[check[0]][check[1]] is EMPTY: break
            if board[check[0]][check[1]] is piece:
                flip(board, piece, move, offset)
                break
            check[0] += offset[0]
            check[1] += offset[1]
    return

def flip(board, piece, move, offset):
    check = [move[0]+offset[0], move[1]+offset[1]]
    while(board[check[0]][check[1]] is inverse(piece)):
        board[check[0]][check[1]] = piece
        check[0] += offset[0]
        check[1] += offset[1]
    return

def has_valid_move(board, piece):
    for y in range(board_size):
        for x in range(board_size):
            if is_valid_move(board, piece, (y,x)): return True
    return False

def print_valid_move(board, piece):
    # listValidmove = []
    string = 'abcdefgh'
    validchoice = ''
    for y in range(board_size):
        for x in range(board_size):
            if is_valid_move(board, piece, (y,x)):
                # listValidmove.append((y,x))
                validchoice = validchoice + string[y-1] + str(x) + ' '
    # print(listValidmove)
    print("Valid Choice: ",validchoice)

if __name__ == '__main__':
    main()
