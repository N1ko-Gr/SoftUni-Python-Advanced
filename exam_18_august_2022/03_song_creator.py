import os


def add_songs(*args):
    dict_song = {}

    for song, lyrics in args:
        if song not in dict_song:
            dict_song[song] = []
        if lyrics:
            dict_song[song].append(lyrics)

    result = ''


    for song,lyric in dict_song.items():
        result += f'- {song}\n'
        for lyri in lyric:
            result += '\n'.join(lyri)
            result += '\n'

    return result


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),))

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
