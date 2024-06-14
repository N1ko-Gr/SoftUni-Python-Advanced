def even_odd(*args):
    cmd = args[-1]
    if cmd == 'even':
        return [x for x in args[:-1] if x % 2 == 0]
    elif cmd == 'odd':
        return [x for x in args[:-1] if x % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))