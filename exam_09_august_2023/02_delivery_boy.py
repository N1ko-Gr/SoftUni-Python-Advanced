row, col = map(int, input().split())

matrix = [list(x for x in input()) for _ in range(row)]

delivery_boy_poss = 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(row):
    for c in range(col):
        if matrix[r][c] == 'B':
            delivery_boy_poss = r, c
            matrix[r][c] = ' '

final_boy_pos = delivery_boy_poss

while True:

    cmd = input()
    curr_row = delivery_boy_poss[0] + directions[cmd][0]
    curr_col = delivery_boy_poss[1] + directions[cmd][1]
    if not (0 <= curr_row < row and 0 <= curr_col < col):
        print(f'The delivery is late. Order is canceled.')
        break

    if matrix[curr_row][curr_col] == '*':
        delivery_boy_poss = curr_row - directions[cmd][0], curr_col - directions[cmd][1]
        continue
    elif matrix[curr_row][curr_col] == '-':
        delivery_boy_poss = curr_row, curr_col
        matrix[curr_row][curr_col] = '.'
    elif matrix[curr_row][curr_col] == 'P':
        delivery_boy_poss = curr_row, curr_col
        matrix[curr_row][curr_col] = 'R'
        print('Pizza is collected. 10 minutes for delivery.')
    elif matrix[curr_row][curr_col] == 'A':
        delivery_boy_poss = curr_row, curr_col
        matrix[curr_row][curr_col] = 'P'
        matrix[final_boy_pos[0]][final_boy_pos[1]] = 'B'
        print('Pizza is delivered on time! Next order...')
        break

    delivery_boy_poss = curr_row, curr_col


[print("".join(matrix[i])) for i in range(row)]
