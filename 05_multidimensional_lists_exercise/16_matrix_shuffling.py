row, col = map(int, input().split())

matrix = [input().split() for _ in range(row)]

while True:
    line = input().split()
    if line[0] == "END":
        break

    if line[0] != "swap" or len(line) != 5:
        print('Invalid input!')
        continue

    if line[0] == "swap":
        row1, col1, row2, col2 = [int(x) for x in line[1:]]
        if 0 <= row1 < row and 0 <= row2 < row and 0 <= col1 < col and 0 <= col2 < col:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]

        else:
            print('Invalid input!')
