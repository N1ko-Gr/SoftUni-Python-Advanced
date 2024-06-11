number_plates = set()

for i in range(int(input())):
    cmd, car_numbers = input().split(", ")

    if cmd == "IN":
        number_plates.add(car_numbers)
    else:
        if car_numbers in number_plates:
            number_plates.remove(car_numbers)


if number_plates:
    print(*number_plates, sep="\n")
else:
    print("Parking Lot is Empty")

