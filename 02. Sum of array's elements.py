#https://www.codewars.com/kata/58f475735e78fde4a2000011

def sum1(arr):
    return sum([el * (i+1) for i,el in enumerate(arr)])


# test.assert_equals(sum1([8, 5, 4]), 30)
# test.assert_equals(sum1([4, 9]), 22)
# test.assert_equals(sum1([1, 2, 3, 4, 5]), 55)