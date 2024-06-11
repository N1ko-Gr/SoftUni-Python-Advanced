
n, m = map(int, input().split())

set_one = set(input() for _ in range(n))
set_two = set(input() for _ in range(m))

print(*set_two.intersection(set_one), sep='\n')


