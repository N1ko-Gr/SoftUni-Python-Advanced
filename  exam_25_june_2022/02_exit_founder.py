ROW = 6

first_player, second_player = input().split(', ')

matrix = [input().split() for x in range(ROW)]

move = 1

poss = input()

row_pos = int(poss[1])
col_pos = int(poss[4])

player_poss = row_pos, col_pos
current_player = None
first_resting = False
second_resting = False

while True:

    current_player_row = player_poss[0]
    current_player_col = player_poss[1]

    if move % 2 != 0:
        current_player = first_player
        if first_resting:
            first_resting = False
            move += 1
            poss = input()
            row_pos = int(poss[1])
            col_pos = int(poss[4])
            player_poss = row_pos, col_pos
            continue
    else:
        current_player = second_player
        if second_resting:
            second_resting = False
            move += 1
            poss = input()
            row_pos = int(poss[1])
            col_pos = int(poss[4])
            player_poss = row_pos, col_pos
            continue

    if matrix[current_player_row][current_player_col] == 'E':
        print(f'{current_player} found the Exit and wins the game!')
        break
    elif matrix[current_player_row][current_player_col] == 'T':
        if current_player == first_player:
            print(f'{first_player} is out of the game! The winner is {second_player}.')
        else:
            print(f'{second_player} is out of the game! The winner is {first_player}.')
        break
    elif matrix[current_player_row][current_player_col] == 'W':
        print(f'{current_player} hits a wall and needs to rest.')
        if current_player == first_player:
            first_resting = True
        else:
            second_resting = True

    move += 1
    poss = input()
    row_pos = int(poss[1])
    col_pos = int(poss[4])

    player_poss = row_pos, col_pos






