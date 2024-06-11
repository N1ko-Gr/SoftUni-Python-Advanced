elements = set()

for _ in range(int(input())):
    line = input().split()
    for el in line:
        elements.add(el)

print(*elements, sep='\n')
