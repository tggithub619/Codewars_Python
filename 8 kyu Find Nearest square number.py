#https://www.codewars.com/kata/5a805d8cafa10f8b930005ba

import math
def nearest_sq(n):
    return round(math.sqrt(n))**2

# test.assert_equals(nearest_sq(1), 1)
#         test.assert_equals(nearest_sq(2), 1)
#         test.assert_equals(nearest_sq(10), 9)
#         test.assert_equals(nearest_sq(111), 121)
#         test.assert_equals(nearest_sq(9999), 10000)

def nearest_sq(n):
    return round(n ** 0.5) ** 2