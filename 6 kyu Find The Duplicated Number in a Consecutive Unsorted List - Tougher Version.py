#https://www.codewars.com/kata/558f0553803bc3c4720000af

def find_dup(arr):
    return [el for el in arr if arr.count(el) > 1][0]

def find_dup(arr):
    return sum(arr) - sum(range(1, max(arr)+1))

def find_dup(arr):
    seen = set()
    for a in arr:
        if a in seen:
            return a
        seen.add(a)


#Test.assert_equals(find_dup([1,1,2,3]), 1)
# Test.assert_equals(find_dup([1,2,2,3]), 2)
# Test.assert_equals(find_dup([5,4,3,2,1,1]), 1)
# Test.assert_equals(find_dup([1,3,2,5,4,5,7,6]), 5)
# Test.assert_equals(find_dup([8,2,6,3,7,2,5,1,4]), 2)