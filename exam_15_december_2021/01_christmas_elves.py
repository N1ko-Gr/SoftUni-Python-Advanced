from collections import deque

elf_energy = deque(int(x) for x in input().split())
materials_in_box = [int(x) for x in input().split()]

toys = 0
turns = 1
energy_used = 0

while materials_in_box and elf_energy:

    if elf_energy[0] < 5:
        elf_energy.popleft()
        continue

    energy = elf_energy.popleft()
    material = materials_in_box.pop()

    if turns % 3 == 0:
        third_time_material = material * 2
        if energy >= third_time_material:
            toys += 2
            energy_used += third_time_material
            if (energy - third_time_material) != 0:
                elf_energy.append(energy - third_time_material + 1)

        else:
            materials_in_box.append(material)
            elf_energy.append(energy * 2)

        turns += 1
        continue

    if turns % 5 == 0:
        if energy >= material:
            energy_used += material
            if (energy - material) != 0:
                elf_energy.append(energy - material)
        else:
            materials_in_box.append(material)
            elf_energy.append(energy * 2)

        turns += 1
        continue

    if energy >= material:
        toys += 1
        energy_used += material
        if (energy - material) != 0:
            elf_energy.append(energy - material + 1)

    else:
        materials_in_box.append(material)
        elf_energy.append(energy * 2)

    turns += 1

print(f'Toys: {toys}')
print(f'Energy: {energy_used}')
if elf_energy:
    print(f"Elves left: {', '.join(map(str, elf_energy))}")
if materials_in_box:
    print(f"Boxes left: {', '.join(map(str, materials_in_box))}")