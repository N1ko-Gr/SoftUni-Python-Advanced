ENTERING_GAME_AMOUNT = 100

row = int(input())

matrix = [list(x for x in input()) for _ in range(row)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

gambler_poss = 0, 0

for r in range(row):
    for c in range(row):
        if matrix[r][c] == 'G':
            gambler_poss = r, c
            matrix[r][c] = '-'

cmd = input()
itIsLost = False

while cmd != 'end':
    curr_row = gambler_poss[0] + directions[cmd][0]
    curr_col = gambler_poss[1] + directions[cmd][1]

    if not (0 <= curr_row < row and 0 <= curr_col < row):
        print('Game over! You lost everything!')
        itIsLost = True
        break
    if matrix[curr_row][curr_col] == 'W':
        ENTERING_GAME_AMOUNT += 100
        matrix[curr_row][curr_col] = '-'
    elif matrix[curr_row][curr_col] == 'P':
        ENTERING_GAME_AMOUNT -= 200
        matrix[curr_row][curr_col] = '-'
        if ENTERING_GAME_AMOUNT <= 0:
            print('Game over! You lost everything!')
            itIsLost = True
            break
    elif matrix[curr_row][curr_col] == 'J':
        matrix[curr_row][curr_col] = '-'
        ENTERING_GAME_AMOUNT += 100000
        print('You win the Jackpot!')
        gambler_poss = curr_row, curr_col
        break
    gambler_poss = curr_row, curr_col

    cmd = input()

matrix[gambler_poss[0]][gambler_poss[1]] = 'G'

if not itIsLost:
    print(f'End of the game. Total amount: {ENTERING_GAME_AMOUNT}$')
    [print("".join(matrix[i])) for i in range(row)]
