#https://www.codewars.com/kata/5a4d303f880385399b000001

import math
def strong_num(num):
    arr = sum([math.factorial(int(el)) for el in str(num)])
    return "STRONG!!!!" if arr == num else "Not Strong !!"


#test.assert_equals(strong_num(1)  , "STRONG!!!!")
# test.assert_equals(strong_num(2)  , "STRONG!!!!")
# test.assert_equals(strong_num(145), "STRONG!!!!")


import math

def strong_num(number):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"