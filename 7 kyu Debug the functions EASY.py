#https://www.codewars.com/kata/5844a422cbd2279a0c000281

import math

def multi(l):
    total = 1
    for i in range(0, len(l)):
        total *= l[i]
    return total

def add(l):
    return sum(l)
def reverse(str):
    return str[::-1]

# test.assert_equals(multi([8,2,5]),80)
# test.assert_equals(add([1,15,3]),19)
# test.assert_equals(add([7,8,6,5,4,9]),39)
# test.assert_equals(reverse("Hello World"),"dlroW olleH")

from functools import reduce
from operator import mul

def multi(l_st):
    return reduce(mul,l_st)
def add(l_st):
    return sum(l_st)
def reverse(s):
    return s[::-1]

