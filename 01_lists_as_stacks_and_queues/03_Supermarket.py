from collections import deque

line = input()
people_in_line = deque()

while line != 'End':

    if line == 'Paid':
        for _ in range(len(people_in_line)):
            print(people_in_line.popleft())
    else:
        people_in_line.append(line)

    line = input()

print(f"{len(people_in_line)} people remaining.")
