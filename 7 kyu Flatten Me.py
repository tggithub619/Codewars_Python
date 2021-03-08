#https://www.codewars.com/kata/55a5bef147d6be698b0000cd

def flatten_me(lst):
    arr = []
    for el in lst:
        if type(el) == list:
            arr.extend(el)
        else:
            arr.append(el)
    return arr

# Test.assert_equals(flatten_me([1, [2, 3], 4]), [1, 2, 3, 4])
# Test.assert_equals(flatten_me([['a', 'b'], 'c', ['d']]), ['a', 'b', 'c', 'd'])
# Test.assert_equals(flatten_me(['!', '?']), ['!', '?'])
# Test.assert_equals(
#     flatten_me([[True, False], ['!'], ['?'], [71, '@']]),
#     [True, False, '!', '?', 71, '@']
# )

