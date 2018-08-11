board_size = 8
BLACK = 'B'
WHITE = 'W'
EMPTY = '.'
offsets = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))

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


print(create_board())
