from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

operator = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 0,
}

total_honey = 0

while bees and nectar:
    if bees[0] > nectar[-1]:
        nectar.pop()
        continue
    else:
        total_honey += abs(operator[symbols.popleft()](bees.popleft(), nectar.pop()))


print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join(map(str, bees))}')
if nectar:
    print(f'Nectar left: {", ".join(map(str, nectar))}')
