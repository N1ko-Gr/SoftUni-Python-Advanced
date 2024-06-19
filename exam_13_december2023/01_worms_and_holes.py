from collections import deque

worms = deque([int(x) for x in input().split()])
holes = deque([int(x) for x in input().split()])
matches = 0
count_worms = len(worms)
count_holes = len(holes)

while worms and holes:
    worm_to_match = worms[-1]
    hole_to_match = holes[0]

    if worm_to_match == hole_to_match:
        worms.pop()
        holes.popleft()
        matches += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()
            continue


if matches:
    print(f'Matches: {matches}')
else:
    print(f'There are no matches.')

if not worms and matches == count_worms:
    print(f'Every worm found a suitable hole!')
elif not worms and matches < count_worms:
    if matches - count_holes < 0:
        print('Worms left: none')
    else:
        print(f'Worms left: {matches - count_worms}')
elif worms:
    print(f'Worms left: {", ".join([str(x) for x in worms])}')

if not holes:
    print('Holes left: none')
else:
    print(f'Holes left: {", ".join([str(x) for x in holes])}')
