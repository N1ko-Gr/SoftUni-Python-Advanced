matrix = []

for x in range(int(input())):
    matrix.append([int(x) for x in input().split()])

line = input().split()

while line[0] != "END":
    cmd = line[0]
    row, cow, number = [int(x) for x in line[1:]]

    if not (0 <= row < len(matrix) and 0 <= cow < len(matrix[0])):
        print('Invalid coordinates')
        line = input().split()
        continue
    elif cmd == "Add":
        matrix[row][cow] += int(number)
    elif cmd == "Subtract":
        matrix[row][cow] -= int(number)

    line = input().split()

[print(*row) for row in matrix]
