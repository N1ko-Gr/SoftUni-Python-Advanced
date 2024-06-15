from collections import deque

tools_sequences = deque(int(x) for x in input().split())
substances_sequences = [int(x) for x in input().split()]
challenges = deque(int(x) for x in input().split())

while tools_sequences and substances_sequences and challenges:
    current_magic = tools_sequences[0] * substances_sequences[-1]

    if current_magic in challenges:
        tools_sequences.popleft()
        challenges.remove(current_magic)
        substances_sequences.pop()

    else:
        tools_sequences[0] += 1
        tools_sequences.rotate(-1)
        substances_sequences[-1] -= 1
        if substances_sequences[-1] == 0:
            substances_sequences.pop()


if not challenges:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')
    if substances_sequences:
        print(f'Substances: {", ".join(map(str, substances_sequences))}')
    if challenges:
        print(f'Challenges: {", ".join(map(str, challenges))}')
else:
    print('Harry is lost in the temple. Oblivion awaits him.')
    print(f'Tools: {", ".join(map(str, tools_sequences))}')
    if substances_sequences:
        print(f'Substances: {", ".join(map(str, substances_sequences))}')
    if challenges:
        print(f'Challenges: {", ".join(map(str, challenges))}')

