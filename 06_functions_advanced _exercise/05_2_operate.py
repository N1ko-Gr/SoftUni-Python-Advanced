def operate(operator, *args):
    if not args:
        return 0

    result2 = args[0]

    if operator == '+':
        result2 = sum(args)
    elif operator == '-':
        for arg in args[1:]:
            result2 -= arg
    elif operator == '*':
        result2 = 1
        for arg in args:
            result2 *= arg
    elif operator == '/':
        for arg in args[1:]:
            result2 /= arg

    return result2


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))