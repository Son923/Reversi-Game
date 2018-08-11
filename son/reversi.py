board_size = 8
BLACK = 'B'
WHITE = 'W'
EMPTY = '.'
offsets = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
black, white = 0,0

# __main__
def reversiMain():
    board = create_board()
    piece = BLACK
    game_loop():


    return

# count_score
def count_score():
    for row in board:
            for token in row:
                if token is WHITE: white += 1
                if token is BLACK: black += 1
    print("End of the game. W: {}, B: {}".format(white,black))
    if black == white:
        print("Draw.")
    else:
        print()
        print('{token} wins.' % (B if black>white else W))


def is_valid_move():



def game_loop(board, piece):
    print()
    print_board(board)
    while(True):
        try:
            move = eval(input('Place %s where? ' % piece))
            move = tuple(reversed(move))
            # x,y -> y,x (easier to use)
            if is_valid_move(board, piece, move):
                place_piece(board, piece, move)
                return
            else:
                raise AssertionError
        except (TypeError, ValueError, IndexError, SyntaxError, AssertionError):
            #   ------------------bad  input------------------  ---bad move---
            print('Invalid move. Try again.')


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
    print(board)
    for row in range(len(board)):
        print(board[row], sep=' ')
def print_board(board):
    for row in range(len(board)):
        print(*board[row], sep='')
    return
