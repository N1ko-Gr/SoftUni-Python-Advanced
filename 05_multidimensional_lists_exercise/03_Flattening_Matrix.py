rows = int(input())
matrix = []

for i in range(rows):
    line = [int(n) for n in input().split(", ")]
    matrix += line

print(matrix)