def accommodate_new_pets(available_capacity, max_weight_limit, *args):
    animals = {}
    result = ''

    for animal, weight in args:
        if available_capacity <= 0:
            result += f'You did not manage to accommodate all pets!'
            break
        if weight > max_weight_limit:
            continue
        if animal not in animals:
            animals[animal] = 0
        animals[animal] += 1
        available_capacity -= 1
    else:
        result += f'All pets are accommodated! Available capacity: {available_capacity}.'

    orderd_pets = sorted(animals.items(), key=lambda x: x[0])

    result += f'\nAccommodated pets:'
    for animal, count in orderd_pets:
        result += f'\n{animal}: {count}'

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))

