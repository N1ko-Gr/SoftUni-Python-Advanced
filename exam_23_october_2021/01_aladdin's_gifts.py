from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

gift = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()

    if (magic + material) < 100:
        total_magic = 0

        if (magic + material) % 2 == 0:
            total_magic = (magic * 3) + (material * 2)
        else:
            total_magic = (magic + material) * 2

        if 100 <= total_magic <= 199:
            gift["Gemstone"] += 1
        elif 200 <= total_magic <= 299:
            gift["Porcelain Sculpture"] += 1
        elif 300 <= total_magic <= 399:
            gift["Gold"] += 1
        elif 400 <= total_magic <= 499:
            gift["Diamond Jewellery"] += 1

    elif 100 <= (magic + material) <= 199:
        gift["Gemstone"] += 1
    elif 200 <= (magic + material) <= 299:
        gift["Porcelain Sculpture"] += 1
    elif 300 <= (magic + material) <= 399:
        gift["Gold"] += 1
    elif 400 <= (magic + material) <= 499:
        gift["Diamond Jewellery"] += 1
    else:
        total_magic_devided = (magic + material) / 2

        if 100 <= total_magic_devided <= 199:
            gift["Gemstone"] += 1
        elif 200 <= total_magic_devided <= 299:
            gift["Porcelain Sculpture"] += 1
        elif 300 <= total_magic_devided <= 399:
            gift["Gold"] += 1
        elif 400 <= total_magic_devided <= 499:
            gift["Diamond Jewellery"] += 1

if (gift["Gemstone"] > 0 and gift["Porcelain Sculpture"] > 0
    or gift["Gold"] > 0 and gift["Diamond Jewellery"] > 0):
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for key, value in sorted(gift.items()):
    if value > 0:
        print(f"{key}: {value}")