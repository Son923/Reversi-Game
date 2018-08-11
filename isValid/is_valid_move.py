def is_valid_move(board, color, move):
    offsets = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
    if board[move[0]][move[1]] is not '.':
        return False
    for offset in offsets:
        check = [move[0]+offset[0], move[1]+offset[1]]
        while 0<=check[0]<board_size-1 and 0<=check[1]<board_size-1 and board[check[0]][check[1]] is inverse(color):
            check[0] += offset[0]
            check[1] += offset[1]
            if board[check[0]][check[1]] is color:
                return True
    return False
def inverse(color):
    return 'B' if piece is 'W'
