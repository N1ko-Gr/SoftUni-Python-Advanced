rows = int(input())
matrix = []
result = ''
for i in range(rows):
    line = [int(n) for n in input().split(", ")]
    matrix.append([])
    for j in line:
        if j % 2 == 0:
            matrix[i].append(j)

print(matrix)
