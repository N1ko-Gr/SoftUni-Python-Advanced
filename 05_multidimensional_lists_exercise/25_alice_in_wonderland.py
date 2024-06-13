size = int(input())
matrix = []
alice_pos = [0, 0]
tea_bags = 0


for row in range(size):
    matrix.append(input().split())
    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[alice_pos[0]][alice_pos[1]] = '*'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

cmd_direction = input()

while True:
    row, col = directions[cmd_direction]

    pos_row = alice_pos[0] + row
    pos_col = alice_pos[1] + col

    if not (0 <= pos_row < size and 0 <= pos_col < size):
        break
    if matrix[pos_row][pos_col] == 'R':
        matrix[pos_row][pos_col] = '*'
        break
    elif matrix[pos_row][pos_col].isdigit():
        tea_bags += int(matrix[pos_row][pos_col])
        matrix[pos_row][pos_col] = '*'
        if tea_bags >= 10:
            break
    else:
        matrix[pos_row][pos_col] = '*'

    alice_pos = [pos_row, pos_col]

    cmd_direction = input()

if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')
[print(*row) for row in matrix]
