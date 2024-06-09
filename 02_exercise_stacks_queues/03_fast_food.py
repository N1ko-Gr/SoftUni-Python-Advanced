from collections import deque

food_quantity = int(input())
list_of_clients = deque([int(X) for X in input().split()])

print(max(list_of_clients))

while food_quantity > 0 and list_of_clients:
    current_quantity = list_of_clients.popleft()
    if current_quantity > food_quantity:
        list_of_clients.appendleft(current_quantity)
        break
    food_quantity -= current_quantity

final = list(list_of_clients)
if list_of_clients:
    print('Orders left:',*list_of_clients )
else:
    print("Orders complete")

