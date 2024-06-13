n = int(input())

matrix = []
diagonal = 0
for i in range(n):
    line = [int(n) for n in input().split()]
    diagonal += line[i]

print(diagonal)
