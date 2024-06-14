def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        result[name] = kwargs[name[0]]

    result = sorted(result.items())

    final = []

    for name, age in result:
        final.append(f'{name} is {age} years old.')

    return '\n'.join(final)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))



