board_size = 8
player = 'A'
BLACK = 'B'
WHITE = 'W'
EMPTY = '.'
offsets = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))

def create_board():
    board = [[EMPTY for x in range(board_size)] for x in range(board_size)]
    half = board_size//2
    board[half-1][half-1] = WHITE
    board[half][half] = WHITE
    board[half-1][half] = BLACK
    board[half][half-1] = BLACK
    return board

def print_board(board):
    alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    board[0].insert(0,'1')
    board[1].insert(0,'2')
    board[2].insert(0,'3')
    board[3].insert(0,'4')
    board[4].insert(0,'5')
    board[5].insert(0,'6')
    board[6].insert(0,'7')
    board[7].insert(0,'8')
    newBoard = '\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in board])
    print(*alpha)
    print(newBoard)
    return



# def create_board():
#     board = [[EMPTY for x in range(8)] for x in range(8)]
#     half = board_size//2
#     board[half][half] = WHITE
#     board[half + 1][half + 1] = WHITE
#     board[half][half + 1] = BLACK
#     board[half + 1][half] = BLACK
#     return board
#
# def print_board(board):
#     alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     # board[0].insert(0,'1')
#     # board[1].insert(0,'2')
#     # board[2].insert(0,'3')
#     # board[3].insert(0,'4')
#     # board[4].insert(0,'5')
#     # board[5].insert(0,'6')
#     # board[6].insert(0,'7')
#     # board[7].insert(0,'8')
#
#     #
#     # printedBoard = board.copy()
#     # printedBoard[0].insert(0,'1')
#     # printedBoard[1].insert(0,'2')
#     # printedBoard[2].insert(0,'3')
#     # printedBoard[3].insert(0,'4')
#     # printedBoard[4].insert(0,'5')
#     # printedBoard[5].insert(0,'6')
#     # printedBoard[6].insert(0,'7')
#     # printedBoard[7].insert(0,'8')
#     #
#     # print(*alpha)
#     # for row in range(len(printedBoard)):
#     #     print(*printedBoard[row], sep=' ')
#     # print(board)
#     print(*alpha)
#     for row in range(len(board)):
#         print(*board[row], sep=' ')


board = create_board()
print_board(board)
