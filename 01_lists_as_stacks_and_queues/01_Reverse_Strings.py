line = list(input())

result = ''

for i in range(len(line)):
    result += line.pop()

print(result)

