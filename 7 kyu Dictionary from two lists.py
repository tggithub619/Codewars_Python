#https://www.codewars.com/kata/5533c2a50c4fea6832000101

def createDict(k, v):
    dct = {}
    while len(k) > len(v):
        v.append(None)
    for i, key in enumerate(k):
        dct[key] = v[i]
    return dct

# test.assert_equals(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3, 'd': None})
# test.assert_equals(createDict(['a', 'b', 'c'], [1, 2, 3, 4]), {'a': 1, 'b': 2, 'c': 3})


def createDict(keys, values):
    if len(keys) > len(values):
        values += [None] * (len(keys) - len(values))

    return {keys[i]: values[i] for i in range(len(keys))}

def createDict(keys, values):
    return {k:(values[i] if i<len(values) else None) for i,k in enumerate(keys)}