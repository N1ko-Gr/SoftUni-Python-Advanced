row = int(input())
car_number = input()

matrix = [input().split() for x in range(row)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

car_poss = 0, 0
distance_covered = 0

cmd = input()

while cmd != "End":
    current_row = car_poss[0] + directions[cmd][0]
    current_col = car_poss[1] + directions[cmd][1]
    distance_covered += 10

    if matrix[current_row][current_col] == "T":
        matrix[current_row][current_col] = "."
        distance_covered += 20

        for r in range(row):
            for c in range(row):
                if matrix[r][c] == 'T':
                    current_row, current_col = r, c
                    matrix[r][c] = "."

    elif matrix[current_row][current_col] == "F":
        matrix[current_row][current_col] = "."
        car_poss = current_row, current_col
        print(f'Racing car {car_number} finished the stage!')
        break

    car_poss = current_row, current_col
    cmd = input()

else:
    print(f'Racing car {car_number} DNF.')
print(f'Distance covered {distance_covered} km.')
matrix[car_poss[0]][car_poss[1]] = "C"

[print(''.join(row)) for row in matrix]