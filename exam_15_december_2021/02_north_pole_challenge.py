rows, cols = input().split(', ')
rows = int(rows)
cols = int(cols)

matrix = [input().split() for x in range(rows)]

santa_poss = 0, 0
decorations = 0
gifts = 0
cookies = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

decorations_to_collect = 0
gifts_to_collect = 0
cookies_to_collect = 0

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'Y':
            santa_poss = r, c
            matrix[r][c] = 'x'

        elif matrix[r][c] == 'D':
            decorations_to_collect += 1

        elif matrix[r][c] == 'G':
            gifts_to_collect += 1

        elif matrix[r][c] == 'C':
            cookies_to_collect += 1

line = input().split('-')
found_all = False

while line[0] != 'End':
    direction_to_go = line[0]
    steps = int(line[1])

    for i in range(steps):
        current_row = (santa_poss[0] + directions[direction_to_go][0]) % rows
        current_col = (santa_poss[1] + directions[direction_to_go][1]) % cols

        if matrix[current_row][current_col] == 'G':
            gifts += 1
            gifts_to_collect -= 1

        elif matrix[current_row][current_col] == 'D':
            decorations += 1
            decorations_to_collect -= 1

        elif matrix[current_row][current_col] == 'C':
            cookies += 1
            cookies_to_collect -= 1

        matrix[current_row][current_col] = 'x'
        if cookies_to_collect == 0 and gifts_to_collect == 0 and decorations_to_collect == 0:
            print(f'Merry Christmas!')
            found_all = True
            santa_poss = current_row, current_col
            break
        santa_poss = current_row, current_col

    if found_all:
        break
    line = input().split('-')

print('You\'ve collected:')
print(f'- {decorations} Christmas decorations')
print(f'- {gifts} Gifts')
print(f'- {cookies} Cookies')

matrix[santa_poss[0]][santa_poss[1]] = 'Y'

for row in matrix:
    print(' '.join(row))
