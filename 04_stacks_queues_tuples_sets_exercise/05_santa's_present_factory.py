from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

present_factory = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

while magic_level and materials:
    total_magic = materials[-1] * magic_level[0]

    if total_magic in presents:
        present_factory[presents[total_magic]] += 1
        magic_level.popleft()
        materials.pop()
        continue

    elif total_magic < 0:
        temp = materials.pop() + magic_level.popleft()
        materials.append(temp)
    elif total_magic > 0:
        magic_level.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic_level[0] == 0:
            magic_level.popleft()

if (present_factory['Doll'] > 0 and present_factory['Wooden train'] > 0 or
        present_factory['Bicycle'] > 0 and present_factory['Teddy bear'] > 0):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for key, val in sorted(present_factory.items()):
    if val > 0:
        print(f'{key}: {val}')