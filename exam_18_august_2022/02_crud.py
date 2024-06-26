ROW = 6

matrix = [input().split() for x in range(row)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

poss = input()

row_pos = int(poss[1])
col_pos = int(poss[4])

line = input().split(', ')

while line[0] != 'Stop':
    cmd = line[0]
    direction_to_go = line[1]
    current_row = row_pos + directions[direction_to_go][0]
    current_col = col_pos + directions[direction_to_go][1]

    if cmd == 'Create':
        value = line[2]
        if matrix[current_row][current_col] == '.':
            matrix[current_row][current_col] = value
    elif cmd == 'Update':
        value = line[2]
        if matrix[current_row][current_col] != '.':
            matrix[current_row][current_col] = value
    elif cmd == 'Delete':
        if matrix[current_row][current_col] != '.':
            matrix[current_row][current_col] = '.'
    elif cmd == 'Read':
        if matrix[current_row][current_col] != '.':
            print(matrix[current_row][current_col])

    row_pos = current_row
    col_pos = current_col
    line = input().split(', ')

[print(" ".join(matrix[i])) for i in range(row)]
