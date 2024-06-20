row, col = map(int, input().split())

matrix = [input().split() for x in range(row)]
players_moves = 0
opponents_touched = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

player_poss = 0, 0

for r in range(row):
    for c in range(col):
        if matrix[r][c] == 'B':
            player_poss = r, c


cmd = input()

while cmd != 'Finish':
    current_row = player_poss[0] + directions[cmd][0]
    current_col = player_poss[1] + directions[cmd][1]

    if not (0 <= current_row < row and 0 <= current_col < col):
        player_poss = current_row - directions[cmd][0], current_col - directions[cmd][1]
        cmd = input()
        continue

    if matrix[current_row][current_col] == 'O':
        player_poss = current_row - directions[cmd][0], current_col - directions[cmd][1]
        cmd = input()
        continue
    elif matrix[current_row][current_col] == 'P':
        matrix[current_row][current_col] = '-'
        players_moves += 1
        opponents_touched += 1
        if opponents_touched == 3:
            break
    else:
        players_moves += 1

    player_poss = current_row, current_col
    cmd = input()

print('Game over!')
print(f'Touched opponents: {opponents_touched} Moves made: {players_moves}')

