from collections import deque

firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

dict_of_effects = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

while firework_effects and explosive_power:

    if (dict_of_effects['Palm Fireworks'] > 2
            and dict_of_effects['Willow Fireworks'] > 2
            and dict_of_effects['Crossette Fireworks'] > 2):
        print('Congrats! You made the perfect firework show!')
        break

    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    effect = firework_effects.popleft()
    power = explosive_power.pop()

    total_power = effect + power

    if total_power % 3 == 0 and total_power % 5 != 0:
        dict_of_effects['Palm Fireworks'] += 1
    elif total_power % 5 == 0 and total_power % 3 != 0:
        dict_of_effects['Willow Fireworks'] += 1
    elif total_power % 5 == 0 and total_power % 3 == 0:
        dict_of_effects['Crossette Fireworks'] += 1
    else:
        effect -= 1
        firework_effects.append(effect)
        explosive_power.append(power)


else:
    print('Sorry. You can\'t make the perfect firework show.')

if firework_effects:
    print(f'Firework Effects left: {", ".join(str(x) for x in firework_effects)}')

if explosive_power:
    print(f'Explosive Power left: {", ".join(str(x) for x in explosive_power)}')

for key, value in dict_of_effects.items():
    print(f"{key}: {value}")
