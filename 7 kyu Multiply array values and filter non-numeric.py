#https://www.codewars.com/kata/55ed875819ae85ca8b00005c

def multiply_and_filter(seq, mult):
    print(seq, mult)
    return [el * mult for el in seq if type(el) in [int, float]]

# test.assert_equals(multiply_and_filter([1,2,3,4], 1.5), [1.5, 3, 4.5, 6])
#     test.assert_equals(multiply_and_filter([1,2,3], 0), [0, 0, 0])
#     test.assert_equals(multiply_and_filter([0,0,0], 2), [0, 0, 0])
#     test.assert_equals(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, []], 3), [3,7.5,30])
#     test.assert_equals(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, [], True, False], 3), [3,7.5,30])
