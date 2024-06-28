def words_sorting(*args):
    final_dict = {}

    for word in args:
        sum_numb = 0
        for letter in word:
            sum_numb += ord(letter)
        final_dict[word] = sum_numb

    if sum(final_dict.values()) % 2 == 0:
        orderd_dict = sorted(final_dict.items(), key=lambda x: x[0])
    else:
        orderd_dict = sorted(final_dict.items(), key=lambda x: -x[1])
    result = ''
    for key, value in orderd_dict:
        result += f'{key} - {value}\n'

    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
