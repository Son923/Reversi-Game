# def displayBoard():
#     boardList = "[['.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', 'W', 'B', '.', '.', '.'],['.', '.', '.', 'B', 'W', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.', '.']]"
#     return boardList

board_size = 8
BLACK = 'B'
WHITE = 'W'
EMPTY = '.'
offsets = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))

def create_board():
    board = [[EMPTY for x in range(8)] for x in range(8)]

    print(board)
    half = board_size//2
    board[half-1][half-1] = WHITE
    board[half][half] = WHITE
    board[half-1][half] = BLACK
    board[half][half-1] = BLACK
    for row in range(len(board)):
        print(*board[row], sep=' ')

print(create_board())
