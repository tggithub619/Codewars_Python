#https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order, max_e):
    print(order, max_e)
    arr = []
    for el in order:
        if arr.count(el) < max_e:
            arr.append(el)
    print(arr)
    return arr

# Test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
# Test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
