numbers_of_presents = int(input())
n = int(input())

matrix = []
stanta_location = 0, 0
nice_kids_present = 0
nice_kids_count = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    matrix.append(input().split())

    if 'S' in matrix[row]:
        stanta_location = row, matrix[row].index('S')
        matrix[row][matrix[row].index('S')] = '-'

    nice_kids_count += matrix[row].count('V')

line = input()

while line != 'Christmas morning':
    r = stanta_location[0] + directions[line][0]
    c = stanta_location[1] + directions[line][1]

    if not (0 <= r < n and 0 <= c < n):
        line = input()
        continue

    if matrix[r][c] == 'V':
        nice_kids_present += 1
        numbers_of_presents -= 1
        matrix[r][c] = '-'
        stanta_location = (r, c)
    elif matrix[r][c] == 'X':
        matrix[r][c] = '-'
        stanta_location = (r, c)
        line = input()
        stanta_location = r, c
        continue
    elif matrix[r][c] == 'C':
        matrix[r][c] = '-'

        for direction, posision in directions.items():
            row = r + posision[0]
            col = c + posision[1]
            if matrix[row][col] == '-':
                continue
            if matrix[row][col] == 'V':
                nice_kids_present += 1
            numbers_of_presents -= 1
            matrix[row][col] = '-'

    stanta_location = (r, c)
    if not numbers_of_presents and nice_kids_present < nice_kids_count:
        print(f'Santa ran out of presents!')
        break

    line = input()


matrix[stanta_location[0]][stanta_location[1]] = 'S'
[print(*row) for row in matrix]

if nice_kids_count == nice_kids_present:
    print(f"Good job, Santa! {nice_kids_present} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count-nice_kids_present} nice kid/s.")

