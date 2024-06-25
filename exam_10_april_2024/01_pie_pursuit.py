from collections import deque

contestants_of_pies = deque(int(x) for x in input().split())
pieces_of_pie = [int(x) for x in input().split()]

while contestants_of_pies and pieces_of_pie:
    contestant = contestants_of_pies[0]
    pieces = pieces_of_pie[-1]

    if contestant < pieces:
        pieces_of_pie[-1] -= contestant
        contestants_of_pies.popleft()
        if pieces_of_pie[-1] == 1 and len(pieces_of_pie) > 1:
            pieces_of_pie[-2] += 1
            pieces_of_pie.pop()

    elif pieces <= contestant:
        contestants_of_pies[0] -= pieces
        if contestants_of_pies[0] <= 0:
            contestants_of_pies.popleft()
        else:
            contestants_of_pies.rotate(-1)
        pieces_of_pie.pop()
    # elif pieces == contestant:
    #     contestants_of_pies.popleft()
    #     pieces_of_pie.pop()


if not pieces_of_pie and not contestants_of_pies:
    print('We have a champion!')
elif contestants_of_pies:
    print('We will have to wait for more pies to be baked!')
    print(f'Contestants left: {", ".join(map(str, contestants_of_pies))}')
elif pieces_of_pie:
    print('Our contestants need to rest!')
    print(f'Pies left: {", ".join(map(str, pieces_of_pie))}')

