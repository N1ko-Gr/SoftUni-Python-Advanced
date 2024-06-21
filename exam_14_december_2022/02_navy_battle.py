row = int(input())

matrix = [list(x for x in input()) for _ in range(row)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

submarine_poss = 0, 0
mines_hits = 0
battle_cruiser = 0

for r in range(row):
    for c in range(row):
        if matrix[r][c] == 'S':
            submarine_poss = r, c
            matrix[r][c] = '-'

cmd = input()

while True:
    current_row = submarine_poss[0] + directions[cmd][0]
    current_col = submarine_poss[1] + directions[cmd][1]

    if matrix[current_row][current_col] == '*':
        mines_hits += 1
        if mines_hits == 3:
            submarine_poss = current_row, current_col
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!')
            break

    elif matrix[current_row][current_col] == 'C':
        battle_cruiser += 1
        if battle_cruiser == 3:
            submarine_poss = current_row, current_col
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            break

    matrix[current_row][current_col] = '-'
    submarine_poss = current_row, current_col
    cmd = input()

matrix[submarine_poss[0]][submarine_poss[1]] = 'S'
[print("".join(matrix[i])) for i in range(row)]
