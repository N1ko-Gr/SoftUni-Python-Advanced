tickets = set()

for ticket in range(int(input())):
    tickets.add((input()))

line = input()

while line != "END":
    if line in tickets:
        tickets.remove(line)

    line = input()

tickets = sorted(tickets)

print(len(tickets))
print(*tickets, sep="\n")
