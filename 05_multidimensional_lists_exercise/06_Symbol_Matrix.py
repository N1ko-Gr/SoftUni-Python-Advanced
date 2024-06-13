n = int(input())

matrix = []
location = ()
is_fount = False

for i in range(n):
    line = input()
    matrix.append(line)

symbol_to_find = input()

for row in range(n):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol_to_find:
            location = (row, col)
            print(location)
            exit()


print(f"{symbol_to_find} does not occur in the matrix")

