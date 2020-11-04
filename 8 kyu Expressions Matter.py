#https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python

def expression_matter(a, b, c):
    res1 = a * (b + c)
    res2 = a * b * c
    res3 = a + b * c
    res4 = (a + b) * c
    res5 = a + b + c
    return max(res1, res2, res3, res4, res5)