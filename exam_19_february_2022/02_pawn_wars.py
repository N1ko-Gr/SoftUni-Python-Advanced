ROWS = 8

matrix = [input().split() for x in range(ROWS)]

white_poss = 0, 0
black_poss = 0, 0
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for r in range(ROWS):
    for c in range(ROWS):
        if matrix[r][c] == 'w':
            white_poss = r, c

        if matrix[r][c] == 'b':
            black_poss = r, c

chessboard = []

for row in range(ROWS, 0, -1):
    current_row = []
    for col in range(ROWS):
        square = columns[col] + str(row)
        current_row.append(square)
    chessboard.append(current_row)

turn = 1

while True:
    if turn % 2 == 1:

        if ((white_poss[0] - 1, white_poss[1] + 1) == black_poss
            or (white_poss[0] - 1, white_poss[1] - 1) == black_poss):
            print(f'Game over! White win, capture on {chessboard[black_poss[0]][black_poss[1]]}.')
            break

        curr_row = white_poss[0] - 1
        curr_col = white_poss[1] + 0

        if chessboard[curr_row][curr_row][-1] == '8':
            print(f'Game over! White pawn is promoted to a queen at {chessboard[curr_row][curr_col]}.')
            break

        white_poss = curr_row, curr_col
    else:
        if ((black_poss[0] - 1, black_poss[1] + 1) == white_poss
                or (black_poss[0] - 1, black_poss[1] - 1) == white_poss):
            print(f'Game over! Black win, capture on {chessboard[white_poss[0]][white_poss[1]]}.')
            break

        curr_row_b = black_poss[0] + 1
        curr_col_b = black_poss[1] + 0

        if chessboard[curr_row_b][curr_col_b][-1] == '1':
            print(f'Game over! Black pawn is promoted to a queen at {chessboard[curr_row_b][curr_col_b]}.')
            break

        black_poss = curr_row_b, curr_col_b

    turn += 1
