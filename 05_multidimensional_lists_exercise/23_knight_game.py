n = int(input())

matrix = [list(x for x in input()) for _ in range(n)]

positions = (
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, 1),
    (2, -1),
    (-1, 2),
    (-2, 1),
    (1, 2),
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_most_attacks_positions = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < n and 0 <= pos_col < n:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_most_attacks_positions = [row, col]

    if knight_most_attacks_positions:
        r, c = knight_most_attacks_positions
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
