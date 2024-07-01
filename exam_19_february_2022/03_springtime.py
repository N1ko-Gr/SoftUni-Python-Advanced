def start_spring(**kwargs):
    new_dict = {}

    for key, value in kwargs.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(key)

    result = ''
    sorted_dict = sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in sorted_dict:
        result += f'{key}:\n'
        sorted_value = sorted(value)
        for item in sorted_value:
            result += f'-{item}\n'

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
