line = tuple(x for x in input())

occ = {}

for n in line:
    occ[n] = line.count(n)

for key, value in sorted(occ.items()):
    print(f'{key}: {value} time/s')
