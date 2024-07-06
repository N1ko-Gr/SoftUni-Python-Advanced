import math

row = int(input())

matrix = [input().split() for x in range(row)]

player_poss = 0, 0
coins = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

player_moves = []

for r in range(row):
    for c in range(row):
        if matrix[r][c] == 'P':
            player_poss = r, c
            player_moves.append(player_poss)
            matrix[r][c] = '0'

cmd = input()

while True:

    current_row = (player_poss[0] + directions[cmd][0]) % row
    current_col = (player_poss[1] + directions[cmd][1]) % row

    if matrix[current_row][current_col] == 'X':
        player_poss = current_row, current_col
        player_moves.append(player_poss)
        coins = math.floor(coins / 2)
        break

    if matrix[current_row][current_col].isdigit():
        player_poss = current_row, current_col
        coins += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = '0'
        player_moves.append(player_poss)

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

    cmd = input()

if coins < 100:
    print(f"Game over! You've collected {coins} coins.")

print(f"Your path:")

var = [', '.join(map(str, x)) for x in player_moves]

for i in var:
    print(f'[{i}]')
