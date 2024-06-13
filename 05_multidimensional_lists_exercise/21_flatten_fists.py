line = [x for x in input().split('|')]

matrix = []

for x in line[::-1]:
    matrix.extend(x.split())

print(*matrix)
