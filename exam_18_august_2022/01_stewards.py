from collections import deque

seats = input().split(', ')
first_numb = deque(int(x) for x in input().split(', '))
second_numb = deque(int(x) for x in input().split(', '))

matches = 0
rotations = 0
list_of_seats = []


for _ in range(10):
    first = first_numb.popleft()
    second = second_numb.pop()
    total_sum = first + second
    rotations += 1
    for seat in seats:
        curr_seat = seat
        if chr(total_sum) == curr_seat[-1]:
            matches += 1
            list_of_seats.append(curr_seat)
            seats.remove(curr_seat)
            break
    else:
        first_numb.append(first)
        second_numb.appendleft(second)

    if matches == 3:
        break

print(f'Seat matches: {", ".join(list_of_seats)}')
print(f'Rotations count: {rotations}')


