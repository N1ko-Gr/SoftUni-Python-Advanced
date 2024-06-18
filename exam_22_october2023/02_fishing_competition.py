QUOTA = 20

row = int(input())

matrix = [list(x for x in input()) for _ in range(row)]

ship_poss = 0, 0
collected_fish = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(row):
    for c in range(row):
        if matrix[r][c] == 'S':
            ship_poss = r, c
            matrix[r][c] = '-'

cmd = input()

issinked = False

while cmd != 'collect the nets':
    curr_row = (ship_poss[0] + directions[cmd][0]) % row
    curr_col = (ship_poss[1] + directions[cmd][1]) % row

    if matrix[curr_row][curr_col].isdigit():
        current_fish = int(matrix[curr_row][curr_col])
        collected_fish += current_fish
        matrix[curr_row][curr_col] = '-'
    elif matrix[curr_row][curr_col] == 'W':
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{curr_row},{curr_col}]')
        issinked = True
        break

    ship_poss = curr_row, curr_col

    cmd = input()

if collected_fish > QUOTA and not issinked:
    print('Success! You managed to reach the quota!')
elif collected_fish < QUOTA and not issinked:
    print(f'You didn\'t catch enough fish and didn\'t reach the quota! You need '
          f'{QUOTA-collected_fish} tons of fish more.')

if collected_fish > 0 and not issinked:
    print(f'Amount of fish caught: {collected_fish} tons.')

if not issinked:
    matrix[ship_poss[0]][ship_poss[1]] = 'S'
    [print("".join(matrix[i])) for i in range(row)]