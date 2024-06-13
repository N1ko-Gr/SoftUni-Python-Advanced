size = int(input())

matrix = [input().split() for x in range(size)]


max_eggs = float('-inf')
direction_final = ''
max_path = []
bunny_row, bunny_col = 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for x in range(size):
    for y in range(size):
        if matrix[x][y] == 'B':
            bunny_row, bunny_col = x, y
            break

for direction, position in directions.items():
    pos_row = bunny_row + position[0]
    pos_col = bunny_col + position[1]
    eggs = 0
    current_path = []

    if not (0 <= pos_row < size and 0 <= pos_col < size):
        continue
    while matrix[pos_row][pos_col] != 'X':

        if matrix[pos_row][pos_col].isdigit():
            eggs += int(matrix[pos_row][pos_col])
            current_path.append([pos_row, pos_col])

        pos_row += position[0]
        pos_col += position[1]
        if not (0 <= pos_row < size and 0 <= pos_col < size):
            break

    if eggs >= max_eggs:
        max_eggs = eggs
        direction_final = direction
        max_path = current_path

print(direction_final)
[print(row) for row in max_path]
print(max_eggs)


