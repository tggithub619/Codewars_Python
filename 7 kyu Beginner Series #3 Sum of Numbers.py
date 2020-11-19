#https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a, b):
    if b < a:
        a, b = b, a
    res = []
    for i in range(a, b + 1):
        res.append(i)
    return sum(res) if a != b else b


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

def get_sum(a,b):
    res = 0
    if b < a:
        a, b = b, a
    for e in range(a, b + 1):
        res += e
    return res