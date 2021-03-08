#https://www.codewars.com/kata/5239f06d20eeab9deb00049b

def fibonacci(n):
    arr = [0,1]
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
    return arr[0:n] if n > 0 else []

# test.assert_equals(fibonacci(4), [0, 1, 1, 2], 'Should work for 4.')
#         test.assert_equals(fibonacci(1), [0], 'Should work for 1 element.')
#         test.assert_equals(fibonacci(0), [], 'Should have 0 elements for 0.')
#         test.assert_equals(fibonacci(-1), [], 'Should have 0 elements for negative input.')
#         test.assert_equals(fibonacci(-14), [], 'Should have 0 elements for negative input.')