from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque([int(x) for x in input().split()])

healing_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    if current_textile + current_medicament == 30:
        healing_items['Patch'] += 1
    elif current_textile + current_medicament == 40:
        healing_items['Bandage'] += 1
    elif current_textile + current_medicament >= 100:
        healing_items['MedKit'] += 1
        if current_textile + current_medicament == 100:
            continue
        sum_to_add_back = (current_textile + current_medicament) - 100
        medicaments[-1] += sum_to_add_back
    else:
        current_medicament += 10
        medicaments.append(current_medicament)


if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
elif not textiles:
    print('Textiles are empty.')
elif not medicaments:
    print('Medicaments are empty.')

ordered_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))

for item, count in ordered_items:
    if count > 0:
        print(f'{item} - {count}')

if medicaments:
    medicaments.reverse()
    print(f'Medicaments left: {", ".join(map(str, medicaments))}')
if textiles:
    print(f'Textiles left: {", ".join(map(str, textiles))}')