from collections import deque

liter_start = int(input())

quantity_liters = liter_start
line_for_water = deque()
line = input()

while line != 'Start':
    line_for_water.append(line)
    line = input()

line = input()

while line != 'End':

    data = line.split()

    if len(data) == 2:

        quantity_liters += int(data[1])

    else:
        water_to_remove = int(data[0])
        if quantity_liters >= water_to_remove:
            print(f"{line_for_water.popleft()} got water")
            quantity_liters -= water_to_remove
        else:
            print(f"{line_for_water.popleft()} must wait")

    line = input()

print(f"{quantity_liters} liters left")
