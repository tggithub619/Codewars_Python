#https://www.codewars.com/kata/55cb0597e12e896ab6000099/train/python

def arithmetic_sequence_sum(a, r, n):
    res = 0
    for i in range(n):
        res += r * i + a
    return res

# test.assert_equals(arithmetic_sequence_sum(3, 2, 20), 440)
# test.assert_equals(arithmetic_sequence_sum(2, 2, 10), 110)
# test.assert_equals(arithmetic_sequence_sum(1, -2, 10), -80)

def arithmetic_sequence_sum(a, r, n):
    return n * (a + a + ( n - 1) * r) / 2

def arithmetic_sequence_sum(a, r, n):
    return sum(a + r*x for x in range(n))