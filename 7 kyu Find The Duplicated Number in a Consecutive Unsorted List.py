#https://www.codewars.com/kata/558dd9a1b3f79dc88e000001

def find_dup(arr):
    return [el for el in arr if arr.count(el) > 1][0]

#
# Test.assert_equals(find_dup([5, 4, 3, 2, 1, 1]), 1)
# Test.assert_equals(find_dup([1, 3, 2, 5, 4, 5, 7, 6]), 5)