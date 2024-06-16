from collections import deque

armor_values = deque(int(x) for x in input().split(','))
soldier_strike_power = [int(x)for x in input().split(',')]

total_monsters_killed = 0

while armor_values and soldier_strike_power:
    if armor_values[0] <= soldier_strike_power[-1]:
        total_monsters_killed += 1
        soldier_strike_power[-1] -= armor_values.popleft()
        if soldier_strike_power[-1] == 0:
            soldier_strike_power.pop()
            continue
        if len(soldier_strike_power) > 1:
            temp_power = soldier_strike_power.pop()
            soldier_strike_power[-1] += temp_power

    else:
        armor_values[0] -= soldier_strike_power[-1]
        soldier_strike_power.pop()
        armor_values.rotate(-1)

if not armor_values:
    print(f'All monsters have been killed!')
if not soldier_strike_power:
    print(f'The soldier has been defeated.')
print(f'Total monsters killed: {total_monsters_killed}')



