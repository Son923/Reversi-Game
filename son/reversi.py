black = 20
white = 21

# __main__
# count_score
# for row in board:
        # for token in row:
        #     if token is WHITE: white += 1
        #     if token is BLACK: black += 1
print("End of the game. W: {}, B: {}".format(white,black))
if black == white:
    print("Draw.")
else:
    print()
    print('{token} wins.' % (B if black>white else W))
