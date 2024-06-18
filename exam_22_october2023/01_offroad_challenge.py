from collections import deque, defaultdict

initial_fuel = [int(x) for x in input().split()]
additional_consumption = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())

altitudes = len(amount_of_fuel_needed)
current_altitude = 0
altitudes_list = []

while additional_consumption and altitudes and amount_of_fuel_needed:
    current_fuel = initial_fuel.pop()
    current_additional_consumption = additional_consumption.popleft()
    total_fuel_needed = current_fuel - current_additional_consumption

    if total_fuel_needed >= amount_of_fuel_needed[0]:
        current_altitude += 1
        altitudes_list.append(current_altitude)
        amount_of_fuel_needed.popleft()

        print(f'John has reached: Altitude {current_altitude}')
        if altitudes == current_altitude:
            print('John has reached all the altitudes and managed to reach the top!')
            break
    else:
         print(f'John did not reach: Altitude {current_altitude + 1}')
         break

if current_altitude < altitudes:
    print("John failed to reach the top.")
    if current_altitude == 0:
       print("John didn't reach any altitude.")
    else:
        result = 'Reached altitudes: ' + ', '.join(f'Altitude {i}' for i in range(1, current_altitude + 1))
        print(result)


