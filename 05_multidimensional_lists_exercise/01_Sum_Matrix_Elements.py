row, col = [int(n) for n in (input().split(", "))]
matrix = []
sum_total = 0

for i in range(row):
    items = [int(n) for n in input().split(", ")]
    sum_total += sum(items)
    matrix.append(items)

print(sum_total)
print(matrix)

