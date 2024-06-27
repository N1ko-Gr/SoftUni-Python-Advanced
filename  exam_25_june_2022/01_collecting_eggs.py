from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = deque(int(x) for x in input().split(', '))

boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()

    if egg == 13:
        paper_last = papers.popleft()
        papers.appendleft(paper)
        papers.append(paper_last)
        continue

    if egg <= 0:
        papers.append(paper)
        continue

    elif (egg + paper) <= 50:
        boxes += 1

if boxes:
    print(f'Great! You filled {boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(str(x) for x in eggs)}')
if papers:
    print(f'Pieces of paper left: {", ".join(str(x) for x in papers)}')


