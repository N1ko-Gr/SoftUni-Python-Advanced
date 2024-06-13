n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - 1 - i] for i in range(n)]

abs_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(abs_difference)
