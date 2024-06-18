def team_lineup(*args):
    result = ''
    players_dict = {}

    for player, nationality in args:
        if nationality not in players_dict:
            players_dict[nationality] = []
        players_dict[nationality].append(player)

    players_dict_sorted = sorted(players_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for name, players in players_dict_sorted:
        result += f'{name}:\n'
        for player in players:
            result += f'  -{player}\n'

    return result




print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

