#https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

#  test.assert_equals(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
#         test.assert_equals(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
#         test.assert_equals(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
#         test.assert_equals(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
#         test.assert_equals(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
#         test.assert_equals(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
#         test.assert_equals(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
#         test.assert_equals(is_triangle(2, 5, 1), False, "didn't work when sides were 2, 5, 1")
