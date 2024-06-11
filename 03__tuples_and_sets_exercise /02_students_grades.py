n = int(input())

students = {}

for i in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in students:
        students[name] = []

    students[name].append(grade)

for name, grades in students.items():
        average = sum(grades) / len(grades)
        print(f"{name} -> {' '.join([f'{g:.2f}' for g in grades])} (avg: {average:.2f})")





