#https://www.codewars.com/kata/5a662a02e626c54e87000123

def extra_perfect(n):
    arr = []
    for el in range(1, n+1, 2):
        arr.append(el)
    return arr


# Test.assert_equals(extra_perfect(3), [1,3])
# Test.assert_equals(extra_perfect(5), [1,3,5])
# Test.assert_equals(extra_perfect(7), [1,3,5,7])
# Test.assert_equals(extra_perfect(28), [1,3,5,7,9,11,13,15,17,19,21,23,25,27])
# Test.assert_equals(extra_perfect(39), [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39])

def extra_perfect(n):
    return list(range(1,n+1,2))

def extra_perfect(n):
    return [i for i in range(n+1) if i % 2 != 0] 