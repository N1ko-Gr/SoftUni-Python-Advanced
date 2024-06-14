def concatenate(*args, **kwargs):
    concat_string = ''.join(args)

    for key, value in kwargs.items():
        concat_string = concat_string.replace(key, value)

    return concat_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
