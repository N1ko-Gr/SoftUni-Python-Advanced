HEALT = 100

row = int(input())

matrix = [list(x for x in input()) for _ in range(row)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

traveller_poss = 0, 0


for r in range(row):
    for c in range(row):
        if matrix[r][c] == 'P':
            traveller_poss = r, c
            matrix[r][c] = '-'

cmd = input()

while True:
    curr_row = traveller_poss[0] + directions[cmd][0]
    curr_col = traveller_poss[1] + directions[cmd][1]

    if not (0 <= curr_row < row and 0 <= curr_col < row):
        cmd = input()
        continue

    if matrix[curr_row][curr_col] == 'M':
        matrix[curr_row][curr_col] = '-'
        if HEALT <= 40:
            HEALT -= 40
            traveller_poss = curr_row, curr_col
            print('Player is dead. Maze over!')
            break

        HEALT -= 40
    elif matrix[curr_row][curr_col] == 'H':
        HEALT += 15
        if HEALT > 100:
            HEALT = 100
        matrix[curr_row][curr_col] = '-'
    elif matrix[curr_row][curr_col] == 'X':
        traveller_poss = curr_row, curr_col
        print('Player escaped the maze. Danger passed!')
        break

    traveller_poss = curr_row, curr_col
    cmd = input()

if HEALT < 0:
    HEALT = 0

print(f'Player\'s health: {HEALT} units')
matrix[traveller_poss[0]][traveller_poss[1]] = 'P'
[print("".join(matrix[i])) for i in range(row)]