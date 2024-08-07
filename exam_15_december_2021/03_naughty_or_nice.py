def naughty_or_nice_list(*args, **kwargs):
    result = {"Nice": [],
              "Naughty": [],
              "Not found": []}
    output, list_with_names = "", args[0]

    for data in args[1:]:
        number, type_ = [int(x) if x.isdigit() else x for x in data.split("-")]
        if sum(1 for num, name in list_with_names if number == num) == 1:
            for pos, (num, name) in enumerate(list_with_names):
                if number == num:
                    result[type_].append(name)
                    del list_with_names[pos]

    for k_name, v_type in kwargs.items():
        if sum(1 for num, name in list_with_names if k_name == name) == 1:
            for pos,(num, name) in enumerate(list_with_names):
                 if k_name == name:
                    result[v_type].append(name)
                    del list_with_names[pos]

    result["Not found"] = [not_found_name for _, not_found_name in list_with_names]
    for p_type,p_names in result.items():
        if p_names:
            output += f"{p_type}: {', '.join(p_names)}\n"

    return output


print(naughty_or_nice_list(
        [
            (3, "Amy"),
            (1, "Tom"),
            (7, "George"),
            (3, "Katy"),
        ],
        "3-Nice",
        "1-Naughty",
        Amy="Nice",
        Katy="Naughty",
    ))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
