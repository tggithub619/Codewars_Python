#https://www.codewars.com/kata/6000883ce39ca6002648e7f2

import math
def factorial_sum(string):
    s = ""
    for el in string:
        if el.isdigit():
            s += el
        else:
            s += " "
    return sum([math.factorial(int(el)) for el in s.split()])

# test.assert_equals(factorial_sum("8D8"), 80640)
# test.assert_equals(factorial_sum("5H4H19H3H2H18H2"), 128047474114560154)
# test.assert_equals(factorial_sum("11q8"), 39957120)