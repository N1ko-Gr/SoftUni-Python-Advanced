def numbers(*args):
    result_poss = 0
    result_negs = 0
    for num in args:
        if num < 0:
            result_negs += num
        elif num > 0:
            result_poss += num

    return result_poss, result_negs


input_line = [int(x) for x in input().split()]

poss, negative = numbers(*input_line)

print(negative)
print(poss)
if abs(negative) > poss:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')



