from collections import deque

MAX_CAFFEINE_PER_NIGHT = 300

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))

starting_caffeine = 0

while energy_drinks and milligrams_of_caffeine:
    milligrams = milligrams_of_caffeine[-1]
    energy = energy_drinks[0]
    total_energy = milligrams * energy

    if total_energy + starting_caffeine > MAX_CAFFEINE_PER_NIGHT:
        milligrams_of_caffeine.pop()
        energy_drinks.rotate(-1)
        starting_caffeine -= 30
        if starting_caffeine < 0:
            starting_caffeine = 0

    else:
        starting_caffeine += total_energy
        milligrams_of_caffeine.pop()
        energy_drinks.popleft()

if energy_drinks:
    print(f'Drinks left: {", ".join(map(str, energy_drinks))}')
else:
    print(f'At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f'Stamat is going to sleep with {starting_caffeine} mg caffeine.')