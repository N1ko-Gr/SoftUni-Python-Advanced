def shopping_list(budget, **kwargs):

    if budget < 100:
        return f"You do not have enough budget."

    count_of_items = 0
    result = ''

    for key, value in kwargs.items():
        total_amount = value[0] * value[1]
        if total_amount > budget:
            continue
        budget -= total_amount
        result += f"You bought {key} for {total_amount:.2f} leva.\n"
        count_of_items += 1
        if count_of_items == 5:
            break

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))


print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
