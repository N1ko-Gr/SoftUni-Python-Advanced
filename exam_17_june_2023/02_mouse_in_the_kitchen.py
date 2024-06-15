row, col = map(int, input().split(','))

matrix = [list(x for x in input()) for _ in range(row)]


mouse_poss = 0, 0
pieces_of_cheese = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(row):
    for c in range(col):
        if matrix[r][c] == 'M':
            mouse_poss = r, c
            matrix[r][c] = '*'
        if matrix[r][c] == 'C':
            pieces_of_cheese += 1

cmd = input()

while cmd != 'danger':
    curr_row = mouse_poss[0] + directions[cmd][0]
    curr_col = mouse_poss[1] + directions[cmd][1]

    if not (0 <= curr_row < row and 0 <= curr_col < col):
        matrix[curr_row - directions[cmd][0]][curr_col - directions[cmd][1]] = 'M'
        print("No more cheese for tonight!")
        break
    if matrix[curr_row][curr_col] == 'C':
        matrix[curr_row][curr_col] = '*'
        pieces_of_cheese -= 1
        if pieces_of_cheese == 0:
            matrix[curr_row][curr_col] = 'M'
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[curr_row][curr_col] == 'T':
        matrix[curr_row][curr_col] = 'M'
        print("Mouse is trapped!")
        break
    elif matrix[curr_row][curr_col] == '@':
        mouse_poss = curr_row - directions[cmd][0], curr_col - directions[cmd][1]
        cmd = input()
        continue

    mouse_poss = curr_row, curr_col
    cmd = input()

[print("".join(matrix[i])) for i in range(row)]
