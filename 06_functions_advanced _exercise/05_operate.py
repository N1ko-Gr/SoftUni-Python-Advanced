from functools import reduce


def operate(operator, *args):
    mapper = {
        '+': lambda nums: reduce(lambda x, y: x + y, nums),
        '-': lambda nums: reduce(lambda x, y: x - y, nums),
        '*': lambda nums: reduce(lambda x, y: x * y, nums),
        '/': lambda nums: reduce(lambda x, y: x / y, nums),
    }

    return mapper[operator](args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))


