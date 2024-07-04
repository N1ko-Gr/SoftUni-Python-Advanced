ROW = 6

matrix = [input().split() for x in range(ROW)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
}

score = 0

for _ in range(3):
    coord_str = input().strip("()")
    row, column = coord_str.split(", ")
    curr_row = int(row)
    curr_col = int(column)

    if not (0 <= curr_row < ROW and 0 <= curr_col < ROW):
        continue

    if matrix[curr_row][curr_col] == 'B':
        matrix[curr_row][curr_col] = 0

        for r in range(6):
            score += int(matrix[r][curr_col])


if 100 <= score <= 199:
    print(f"Good job! You scored {score} points, and you've won Football.")
elif 200 <= score <= 299:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
elif score >= 300:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100-score} points more to win a prize.")