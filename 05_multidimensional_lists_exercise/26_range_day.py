SIZE = 5

matrix = []
targets_pos = []
shooter_pos = (0, 0)
targets = 0
shot_targets = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Reading the matrix and initializing the shooter's position and target count
for i in range(SIZE):
    row = input().split()
    matrix.append(row)

    if 'A' in row:
        shooter_pos = (i, row.index('A'))

    targets += row.count('x')

# Reading and executing commands
for _ in range(int(input())):
    line = input().split()
    cmd = line[0]
    direction = line[1]

    current_row, current_col = shooter_pos

    if cmd == 'shoot':
        while True:
            current_row += directions[direction][0]
            current_col += directions[direction][1]

            if not (0 <= current_row < SIZE and 0 <= current_col < SIZE):
                break

            if matrix[current_row][current_col] == 'x':
                shot_targets += 1
                matrix[current_row][current_col] = '.'
                targets_pos.append([current_row, current_col])
                break

        if targets == shot_targets:
            print(f'Training completed! All {targets} targets hit.')
            break

    elif cmd == 'move':
        steps = int(line[2])
        new_row = current_row + directions[direction][0] * steps
        new_col = current_col + directions[direction][1] * steps

        if not (0 <= new_row < SIZE and 0 <= new_col < SIZE):
            continue
        if matrix[new_row][new_col] != '.':
            continue

        matrix[shooter_pos[0]][shooter_pos[1]] = '.'
        matrix[new_row][new_col] = 'A'
        shooter_pos = (new_row, new_col)

# Output results
if targets > shot_targets:
    print(f'Training not completed! {targets - shot_targets} targets left.')

for pos in targets_pos:
    print(pos)
