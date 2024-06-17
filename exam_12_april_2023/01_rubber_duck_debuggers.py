from collections import deque

programmer_time = deque([int(x) for x in input().split()])
tasks_to_complete = [int(x) for x in input().split()]

ducks_dic = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0

}

while programmer_time and tasks_to_complete:
    current_time = programmer_time.popleft()
    current_task = tasks_to_complete.pop()

    time_needed = current_time * current_task

    if 0 <= time_needed <= 60:
        ducks_dic['Darth Vader Ducky'] += 1
    elif 61 <= time_needed <= 120:
        ducks_dic['Thor Ducky'] += 1
    elif 121 <= time_needed <= 180:
        ducks_dic['Big Blue Rubber Ducky'] += 1
    elif 181 <= time_needed <= 240:
        ducks_dic['Small Yellow Rubber Ducky'] += 1
    else:
        programmer_time.append(current_time)
        tasks_to_complete.append(current_task - 2)

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
for duck, num in ducks_dic.items():
    print(f'{duck}: {num}')



