#https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9

def up_array(arr):
    if arr == []:
        return None
    for el in arr:
        if el < 0 or el > 9:
            return None
    s = "".join([str(el) for el in arr])
    s = int(s) + 1
    s = [int(el) for el in list(str(s))]
    return s

# Test.assert_equals(up_array([2,3,9]), [2,4,0])
# Test.assert_equals(up_array([4,3,2,5]), [4,3,2,6])
# Test.assert_equals(up_array([1,-9]), None)