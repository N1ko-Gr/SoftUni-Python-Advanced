from collections import deque

bowl_ramen = [int(x) for x in input().split(',')]
customers = deque(int(x) for x in input().split(', '))

while bowl_ramen and customers:
    bowl = bowl_ramen[-1]
    customer = customers[0]

    if bowl == customer:
        customers.popleft()
        bowl_ramen.pop()
    elif bowl > customer:
        bowl_ramen[-1] -= customer
        customers.popleft()
    elif bowl < customer:
        customers[0] -= bowl
        bowl_ramen.pop()

if not customers:
    print('Great job! You served all the customers.')
if bowl_ramen:
    print(f'Bowls of ramen left: {", ".join(str(x) for x in bowl_ramen)}')
if not bowl_ramen and customers:
    print('Out of ramen! You didn\'t manage to serve all customers.')
    print(f'Customers left: {", ".join(str(x) for x in customers)}')


