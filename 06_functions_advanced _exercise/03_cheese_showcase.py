def sorting_cheeses(**kwargs):
    result = ''
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, value in sorted_cheese:
        result += f'{key}\n'
        rev_value = sorted(value, reverse=True)
        for item in rev_value:
            result += f'{item}\n'

    return result




print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

