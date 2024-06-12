from collections import deque

line = input().split()
operator = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x // y,
}

numbers = deque()

for ch in line:
    if ch not in '*+-/':
        numbers.append(int(ch))
    else:
        while len(numbers) > 1:
            a, b = numbers.popleft(), numbers.popleft()
            numbers.appendleft(operator[ch](a, b))

print(*numbers)

