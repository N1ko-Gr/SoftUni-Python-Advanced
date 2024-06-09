from collections import deque

amount_of_pumps = int(input())

information = deque()

for i in range(amount_of_pumps):
    petrol, distance = input().split()
    information.append([int(petrol), int(distance)])

petrol_pump_stops = 0

index_of_pump = 0

while petrol_pump_stops < amount_of_pumps:
    petrol = 0
    for i in range(amount_of_pumps):
        petrol += information[i][0]
        distance = information[i][1]
        if petrol < distance:
            index_of_pump += 1
            petrol_pump_stops = 0
            information.rotate(-1)
            break

        petrol -= distance
        petrol_pump_stops += 1


print(index_of_pump)
