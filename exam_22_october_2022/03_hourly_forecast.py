def forecast(*args):
    dict = {}

    for town, weather_data in args:
        dict[town] = weather_data

    sorted_dict = sorted(dict.items(), key=lambda item: (item[1], item[0]))
    sunny = ''
    cloudy = ''
    rainy= ''

    for town, weather_data in sorted_dict:
        if weather_data == 'Sunny':
            sunny += f'{town} - {weather_data}\n'
        elif weather_data == 'Cloudy':
            cloudy += f'{town} - {weather_data}\n'
        elif weather_data == 'Rainy':
            rainy += f'{town} - {weather_data}\n'

    return sunny + cloudy + rainy


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

