#https://www.codewars.com/kata/586ec0b8d098206cce001141

def inverse_slice(items, a, b):
    del items[a:b]
    return items

def inverse_slice(items, a, b):
    return items[:a] + items[b:]