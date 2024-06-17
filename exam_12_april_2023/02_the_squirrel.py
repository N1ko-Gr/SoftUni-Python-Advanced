row = int(input())

commands = [x for x in input().split(', ')]

matrix = [list(x for x in input()) for _ in range(row)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

hazelnuts = 0
hazelnuts_on_map = 0
squirrels_poss = 0, 0

for r in range(row):
    for c in range(row):
        if matrix[r][c] == 's':
            squirrels_poss = r, c

        if matrix[r][c] == 'h':
            hazelnuts_on_map += 1

for command in commands:
    current_row = squirrels_poss[0] + directions[command][0]
    current_col = squirrels_poss[1] + directions[command][1]

    if not (0 <= current_row < row and 0 <= current_col < row):
        print('The squirrel is out of the field.')
        break
    if matrix[current_row][current_col] == 'h':
        hazelnuts += 1
        matrix[current_row][current_col] = '*'
        if hazelnuts == 3:
            print('Good job! You have collected all hazelnuts!')
            break
    elif matrix[current_row][current_col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        break
    squirrels_poss = current_row, current_col
else:
    print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {hazelnuts}')

