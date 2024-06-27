SOUP = 3
PIZZA = 4
DESSERT = 2


def shopping_cart(*args):
    shopping_cart_product = {
        'Pizza': [],
        'Dessert': [],
        'Soup': []
    }
    result = ''

    for arg in args:
        if arg == 'Stop':
            break
        item = arg[0]
        product = arg[1]

        if product in shopping_cart_product[item]:
            continue
        if item == 'Pizza' and len(shopping_cart_product[item]) == PIZZA:
            continue
        if item == 'SOUP' and len(shopping_cart_product[item]) == SOUP:
            continue
        if item == 'DESSERT' and len(shopping_cart_product[item]) == DESSERT:
            continue
        shopping_cart_product[item].append(product)

    if (not shopping_cart_product['Pizza'] and
            not shopping_cart_product['Dessert'] and
            not shopping_cart_product['Soup']):
        return f'No products in the cart!'

    sorted_products = sorted(shopping_cart_product.items(), key=lambda x: (-len(x[1]), x[0]))

    for i,pr in sorted_products:
        result += f'{i}:\n'
        sorted_pr = sorted(pr)
        for items in sorted_pr:
            result += f' - {items}\n'

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
