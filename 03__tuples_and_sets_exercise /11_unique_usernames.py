names_list = set()

for i in range(int(input())):
    names_list.add(input())

print(*names_list, sep='\n')