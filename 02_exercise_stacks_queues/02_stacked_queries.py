n = int(input())
numbers = []

type_of_command = {
    '1': lambda x: numbers.append(int(x)),
    '2': lambda: numbers.pop() if numbers else None,
    '3': lambda: print(max(numbers)) if numbers else None,
    '4': lambda: print(min(numbers)) if numbers else None,

}

for _ in range(n):
    command = input().split()
    type_of_command[command[0]](*command[1:])

numbers.reverse()
print(*numbers, sep=', ')
