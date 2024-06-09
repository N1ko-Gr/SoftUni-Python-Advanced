stack_of_clouts = [int(x) for x in input().split()]
racks_capacity = int(input())

racks_used = 0

while len(stack_of_clouts) > 1:
    current_capacity = racks_capacity
    while stack_of_clouts and current_capacity >= stack_of_clouts[-1] :
        current_capacity -= stack_of_clouts.pop()

    racks_used += 1

if stack_of_clouts:
    racks_used += 1

print(racks_used)

