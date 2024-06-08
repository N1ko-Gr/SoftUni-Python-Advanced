line = input()

opened_parenthesis = []
index_opened_parenthesis = 0

for char in range(len(line)):

    if line[char] == '(':
        opened_parenthesis.append(char)

    elif line[char] == ')':
        index = opened_parenthesis.pop()
        print(line[index:char+1])
