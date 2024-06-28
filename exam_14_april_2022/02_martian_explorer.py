ROW = 6

matrix = [input().split() for x in range(ROW)]

rover_poss = 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(ROW):
    for c in range(ROW):
        if matrix[r][c] == 'E':
            rover_poss = r, c
            matrix[r][c] = '-'

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

command = input().split(', ')

for cmd in command:
    curr_row = (rover_poss[0] + directions[cmd][0]) % ROW
    curr_col = (rover_poss[1] + directions[cmd][1]) % ROW

    if matrix[curr_row][curr_col] == 'W':
        water_deposit += 1
        print(f'Water deposit found at ({curr_row}, {curr_col})')

    elif matrix[curr_row][curr_col] == 'M':
        metal_deposit += 1
        print(f'Metal deposit found at ({curr_row}, {curr_col})')

    elif matrix[curr_row][curr_col] == 'C':
        concrete_deposit += 1
        print(f'Concrete deposit found at ({curr_row}, {curr_col})')

    elif matrix[curr_row][curr_col] == 'R':
        print(f'Rover got broken at ({curr_row}, {curr_col})')
        break

    matrix[curr_row][curr_col] = '-'
    rover_poss = curr_row, curr_col

if water_deposit and concrete_deposit and metal_deposit:
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')

