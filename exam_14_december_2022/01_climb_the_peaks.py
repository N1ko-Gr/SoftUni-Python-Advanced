from collections import deque

# Reading input for food supplies and daily stamina
food_supplies = [int(x) for x in input().split(', ')]
daily_stamina = deque([int(x) for x in input().split(', ')])

# Defining mountain peaks and their required efforts
mountain_peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70,
}

# List to keep track of climbed mountains
mountains_climbed = []

# Order of peaks to climb
peaks_to_climb = list(mountain_peaks.items())

while food_supplies and daily_stamina and peaks_to_climb:
    food = food_supplies.pop()
    stamina = daily_stamina.popleft()
    total = food + stamina

    current_peak, required_effort = peaks_to_climb[0]

    if total >= required_effort:
        mountains_climbed.append(current_peak)
        peaks_to_climb.pop(0)  # Remove the peak from the list

if len(mountains_climbed) == 5:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if mountains_climbed:
    print('Conquered peaks:')
    print('\n'.join(mountains_climbed))