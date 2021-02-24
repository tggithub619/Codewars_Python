#https://www.codewars.com/kata/52efefcbcdf57161d4000091

def count(s):
    return {el: s.count(el) for el in s}

# test.assert_equals(count('aba'), {'a': 2, 'b': 1})
# test.assert_equals(count(''), {})

def count(string):
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r