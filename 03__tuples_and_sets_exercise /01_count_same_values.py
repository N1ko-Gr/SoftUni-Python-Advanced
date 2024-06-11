line = tuple(float(x) for x in input().split())

occ = {}

for n in line:
    occ[n] = line.count(n)

for key, value in occ.items():
    print(f'{key} - {value} times')
