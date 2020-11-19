#https://www.codewars.com/kata/55cb0597e12e896ab6000099/train/python

def arithmetic_sequence_sum(a, r, n):
    res = 0
    for i in range(n):
        res += r * i + a
    return res

def arithmetic_sequence_sum(a, r, n):
    return n * (a + a + ( n - 1) * r) / 2  