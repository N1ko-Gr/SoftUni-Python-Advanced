def draw_cards(*args,**kwargs):
    dict_monster = {}
    result = ''

    for name, card in args:
        if card not in dict_monster:
            dict_monster[card] = []
        dict_monster[card].append(name)

    for name, card in kwargs.items():
        if card not in dict_monster:
            dict_monster[card] = []
        dict_monster[card].append(name)

    dict_monster_sorted = sorted(dict_monster.items())

    for name, car in dict_monster_sorted:
        if name == 'monster':
            result += f'Monster cards:\n'
            ordered_items = sorted(car, reverse=True)
            for card in ordered_items:
                result += f'  ***{card}\n'
        if name == 'spell':
            result += f'Spell cards:\n'
            ordered_cards2 = sorted(car)
            for card2 in ordered_cards2:
                result += f'  $$${card2}\n'

    return result


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
