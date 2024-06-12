from collections import deque

chocolate = [int(x) for x in input().split(', ')]
cup_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolate and cup_of_milk and milkshakes < 5:
    if cup_of_milk[0] <= 0 and chocolate[-1] <= 0:
        cup_of_milk.popleft()
        chocolate.pop()
        continue
    if cup_of_milk[0] <= 0:
        cup_of_milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue

    if cup_of_milk[0] == chocolate[-1]:
        milkshakes += 1
        cup_of_milk.popleft()
        chocolate.pop()
        continue
    else:
        cup_of_milk.rotate(-1)
        chocolate[-1] -= 5


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolate:
    print(f"Chocolate: {', '.join(map(str, chocolate))}")
else:
    print('Chocolate: empty')
if cup_of_milk:
    print(f"Milk: {', '.join(map(str, cup_of_milk))}")
else:
    print('Milk: empty')
