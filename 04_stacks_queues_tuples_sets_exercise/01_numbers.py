first_sequences = set([int(x) for x in input().split()])
second_sequences = set([int(x) for x in input().split()])

for _ in range(int(input())):
    line = input().split()
    cmd = line[0] + ' ' + line[1]
    temp_set = [int(x) for x in line[2:]]

    if cmd == 'Add First':
        first_sequences.update(temp_set)
    elif cmd == 'Add Second':
        second_sequences.update(temp_set)
    elif cmd == 'Remove First':
        first_sequences.difference_update(temp_set)
    elif cmd == 'Remove Second':
        second_sequences.difference_update(temp_set)
    elif cmd == 'Check Subset':
        print(first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences))


print(', '.join([str(x) for x in sorted(first_sequences)]))
print(', '.join([str(x) for x in sorted(second_sequences)]))
